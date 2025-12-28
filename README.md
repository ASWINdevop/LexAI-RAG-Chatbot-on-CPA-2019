
# ⚖️ LexAI: Indian Legal Intelligence (CPA 2019)

**An AI-powered legal assistant grounded in the Consumer Protection Act 2019.**

LexAI is a Retrieval-Augmented Generation (RAG) chatbot designed to interpret Indian legal texts. It allows users to ask questions in natural language and receive accurate, context-aware answers strictly based on the provided legal documents.

---

## 🚀 Key Features
* **📚 Accurate Legal Retrieval:** Uses a vector database to find the exact sections of the law relevant to your query.
* **🧠 Gemini 2.5 Flash Integration:** Powered by Google's latest LLM for fast and precise legal reasoning.
* **⚖️ Citation-Backed Answers:** Every response includes the specific "Source Context" from the Act to ensure transparency.
* **💻 Professional UI:** A polished, dark-mode web interface built with Streamlit.
* **🚫 No Hallucinations:** The system is prompted to strictly admit when an answer is not found in the text, preventing false legal advice.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **LLM:** Google Gemini-2.5-Flash
* **Orchestration:** LangChain (LCEL Architecture)
* **Vector Database:** FAISS (Facebook AI Similarity Search)
* **Embeddings:** HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`)
* **Interface:** Streamlit (Web UI)

---

## 📂 Project Structure
```text
RAG PROJECT/
├── data/
│   ├── raw/                  # Contains the CPA 2019 PDF
│   └── processed/            # FAISS Vector Index (saved here)
├── src/
│   ├── preprocess/           # Chunking logic
│   ├── retrieval/            # RAG Chain definition
│   ├── vectordb/             # Vector store management
│   ├── app.py                # CLI Interface (Legacy)
│   ├── ui.py                 # Main Streamlit Web App
│   ├── ingest.py             # Script to build the knowledge base
│   └── logo.png              # App branding
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```
⚙️ Installation & Setup
1. Clone the Repository


git clone [https://github.com/SeionixAi/B115-Aswin-A-S-Phase-4.git](https://github.com/SeionixAi/B115-Aswin-A-S-Phase-4.git)
cd B115-Aswin-A-S-Phase-4

2. Create a Virtual Environment


# Windows
```
python -m venv venv
venv\Scripts\activate
```

# Mac/Linux
```
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies

pip install -r requirements.txt

4. Configure API Key

Create a file named .env in the root directory.

Add your Google Gemini API key:
```
GOOGLE_API_KEY="your_actual_api_key_here"
```

## 🏃‍♂️ Usage Guide
Step 1: Build the Knowledge Base (Run Once)
Before using the bot, you must process the PDF and create the vector database.

```
python src/ingest.py
```
Wait for the message: "Done! Knowledge base is ready."

Step 2: Launch the Web Application
Start the UI:

```
streamlit run src/ui.py
```
The app will open in your browser at http://localhost:8501.

📸 Usage Example
```
User Query: "What are the rights of a consumer?"
```
LexAI Answer:
```

"According to the Consumer Protection Act 2019, a consumer has the following rights:

The right to be protected against marketing of goods hazardous to life.

The right to be informed about the quality, quantity, potency, purity, standard and price of goods..."

Source Citation:

Section Reference 1: "...means the right to be assured, wherever possible, access to a variety of goods, products or services at competitive prices..."
```

⚠️ Limitations & Disclaimer
Scope: This bot interprets only the Consumer Protection Act 2019. It does not know about other laws or recent court judgements outside this text.

LEGAL ADVICE: This tool is for educational and informational purposes only. It is not a substitute for professional legal counsel.



## 🎥 Project Demo

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/ec8088bf-bd17-439c-856b-c77acb6ca086" />


<img width="1915" height="907" alt="Image" src="https://github.com/user-attachments/assets/9c8b638b-71be-45ef-8933-fb5bd23ae80d" />


https://github.com/user-attachments/assets/f0a638b7-18e4-454d-bd5b-c5460daa61aa


