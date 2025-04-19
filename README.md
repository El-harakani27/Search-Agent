# 🤖 AI Search Assistant with LangChain & Streamlit  

*A smart chatbot that answers questions using Wikipedia, arXiv, and web search*  

## ✨ What It Does  
This chatbot lets you:  
- Ask questions naturally (like "Explain quantum computing")  
- Get answers pulled from **Wikipedia**, **arXiv research papers**, and **web search**  
- See the AI's thought process in real-time  

Perfect for researchers, students, or anyone who wants AI-powered answers with sources!  

## 🛠️ Tech Stack  
- **LangChain** (AI agent logic)  
- **Streamlit** (web interface)  
- **Groq API** (for ultra-fast Llama 3 responses)  
- **Wikipedia/arXiv/DuckDuckGo** (data sources)  

## 🚀 Quick Setup  

### 1. Get your API keys  
- Free [Groq API key](https://console.groq.com/keys)  
- (Optional) [Wikipedia](https://www.mediawiki.org/wiki/API:Main_page)/[arXiv](https://arxiv.org/help/api/) keys if rate-limited  

### 2. Run locally  
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -r requirements.txt
streamlit run app.py
