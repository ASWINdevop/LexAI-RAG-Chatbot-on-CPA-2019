import streamlit as st
import sys
import os
import time
import base64

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.retrieval.rag import get_rag_chain

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="LexAI - Legal Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. IMAGE LOADER FUNCTION ---
def get_img_as_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
logo_base64 = get_img_as_base64(logo_path)

if logo_base64:
    logo_src = f"data:image/png;base64,{logo_base64}"
else:
    logo_src = "https://cdn-icons-png.flaticon.com/512/924/924915.png"

# --- 3. Dark Mode & Professional Styling ---
st.markdown("""
<style>
    /* 1. Force Dark Background */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    
    /* 2. Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    
    /* 3. BIGGER Logo & Title */
    .sidebar-logo-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .sidebar-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 2.2rem !important;
        color: #58a6ff !important;
        margin-top: 10px;
        margin-bottom: 0px;
    }
    .sidebar-subtitle {
        font-size: 1.0rem;
        color: #8b949e;
        margin-top: 5px;
    }

    /* 4. Chat Message Bubbles */
    [data-testid="stChatMessage"] {
        background-color: #161b22; 
        border: 1px solid #30363d;
        border-radius: 10px;
    }
    /* ENSURE MARKDOWN RENDERS CLEANLY */
    [data-testid="stChatMessage"] p {
        color: #e6edf3 !important;
        line-height: 1.6; /* Better spacing for reading */
        font-size: 1.05rem;
    }
    [data-testid="stChatMessage"] ul {
        color: #e6edf3 !important;
    }
    
    /* 5. Chat Input Bar */
    .stChatInput {
        padding-bottom: 20px;
    }
    .stChatInput textarea {
        background-color: #0d1117 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
    }

    /* 6. Button Styling */
    .stButton > button {
        width: 100%;
        background-color: #238636;
        color: white !important;
        border: none;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 6px;
    }
    .stButton > button:hover {
        background-color: #2ea043;
        color: white !important;
    }

    /* 7. Headers */
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #58a6ff;
        text-align: center;
    }
    .sub-header {
        text-align: center;
        color: #8b949e;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. Sidebar ---
with st.sidebar:
    st.markdown(f"""
        <div class="sidebar-logo-container">
            <img src="{logo_src}" width="120" style="border-radius: 10px;">
            <div class="sidebar-title">LexAI</div>
            <div class="sidebar-subtitle">Legal Assistant</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("**Active Law:**\nConsumer Protection Act 2019")
    
    st.markdown("""
    **Capabilities:**
    - 🔍 Search legal definitions
    - 📖 Explain consumer rights
    - 📜 Cite specific sections
    """)
    
    st.markdown("---")
    
    def clear_history():
        st.session_state.messages = []
    
    if st.button("✨ Start New Chat", on_click=clear_history):
        st.rerun()

    st.markdown("---")
    st.caption("© 2025 LexAI | Powered by Google Gemini")

# --- 5. Main Chat ---

st.markdown('<div class="main-header">LexAI: Indian Legal Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Ask questions about the Consumer Protection Act 2019</div>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "👋 **Hello!** I am LexAI.\n\nI can help you interpret the **Consumer Protection Act 2019**. Ask me about:\n* Unfair trade practices\n* Product liability\n* How to file a complaint"
    })

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 6. Logic ---
if prompt := st.chat_input("Type your legal question here..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.spinner("⚖️ Consulting the Act..."):
            try:
                time.sleep(0.5) 
                
                rag_chain = get_rag_chain()
                response = rag_chain.invoke(prompt)
                
                answer = response['answer']
                sources = response['source_documents']
                
                # Display Answer (Streamlit renders Markdown automatically)
                message_placeholder.markdown(answer)
                
                if sources:
                    with st.expander("🔍 View Legal Source Text"):
                        for i, doc in enumerate(sources):
                            st.markdown(f"**Section Reference {i+1}:**")
                            # Clean up newlines in source text specifically
                            clean_source = doc.page_content.replace("\n", " ")
                            st.markdown(f"> {clean_source[:400]}...")
                            st.markdown("---")
                
                st.session_state.messages.append({"role": "assistant", "content": answer})

            except Exception as e:
                message_placeholder.error(f"⚠️ Error: {str(e)}")