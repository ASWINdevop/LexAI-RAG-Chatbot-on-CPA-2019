import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from src.vectordb.store import load_vector_db

load_dotenv()

def format_docs(docs):
    """Helper to join document content into a single string"""
    return "\n\n".join(doc.page_content for doc in docs)

def get_rag_chain():
    # 1. Load Vector DB
    vector_store = load_vector_db()
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    # 2. Setup LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        temperature=0.3
    )

    # 3. Define Prompt (UPDATED FOR BETTER FORMATTING)
    template = """
    You are a legal assistant for the Consumer Protection Act 2019.
    
    Your goal is to provide clear, easy-to-read legal advice.
    
    INSTRUCTIONS:
    1. Answer the question strictly based on the provided Context.
    2. Format your answer using **Markdown** for readability:
       - Use **Bold** for key terms.
       - Use *Bullet Points* for lists of rights, duties, or conditions.
       - Use > Blockquotes for direct legal definitions.
       - Split long text into short paragraphs.
    3. If the answer is not in the context, say "I cannot find the answer in the provided legal text."
    
    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    prompt = ChatPromptTemplate.from_template(template)

    # 4. Create the Chain (Using LCEL)
    entry_point = RunnableParallel(
        {"context": retriever, "question": RunnablePassthrough()}
    )
    
    retrieval_chain = (
        entry_point
        | {
            "answer": (
                RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"])))
                | prompt
                | llm
                | StrOutputParser()
            ),
            "source_documents": lambda x: x["context"]
        }
    )
    
    return retrieval_chain