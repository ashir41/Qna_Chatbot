# 🤖 AI Chatbot using LangChain + Groq + Google Search

### 🚀 Deployed with Streamlit

An intelligent AI chatbot built using **LangChain**, powered by **Groq
LLM**, and enhanced with **Google Search (Serper API)** for real-time
information retrieval.

This application is deployed using **Streamlit Community Cloud**.

------------------------------------------------------------------------

## 🌐 Live Application

🔗 Live Demo: https://qnachatbotforpractise.streamlit.app/

------------------------------------------------------------------------

## 📦 GitHub Repository

🔗 Source Code: https://github.com/ashir41/Qna_Chatbot

------------------------------------------------------------------------

## 🧠 Project Overview

This chatbot combines the power of Large Language Models with real-time
search capabilities.

It uses: - Groq LLM for ultra-fast response generation - Google Search
(Serper API) to fetch real-world data - LangChain Agent to decide when
to use the LLM or search tool - Streamlit for the interactive web
interface

------------------------------------------------------------------------

## ✨ Features

-   Fast inference using Groq
-   Real-time web search integration
-   LangChain agent-based reasoning
-   Conversational memory
-   Secure API key handling
-   Streamlit web deployment
-   Clean and interactive UI

------------------------------------------------------------------------

## 🏗️ Tech Stack

-   Python
-   LangChain
-   Groq API
-   Serper API (Google Search)
-   Streamlit
-   dotenv



------------------------------------------------------------------------

## ⚙️ Installation (Run Locally)

### 1. Clone the Repository

git clone https://github.com/ashir41/Qna_Chatbot.git\
cd Qna_Chatbot

### 2. Create Virtual Environment

python -m venv venv\
source venv/bin/activate \# Mac/Linux\
venv`\Scripts`{=tex}`\activate         `{=tex}\# Windows

### 3. Install Dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

## 🔐 Environment Variables

Create a `.env` file in the root directory:

GROQ_API_KEY=your_groq_api_key\
SERPER_API_KEY=your_serper_api_key

Do not commit `.env` to GitHub.

------------------------------------------------------------------------

## ▶️ Run the Application

streamlit run app.py

The app will run at: http://localhost:8501

------------------------------------------------------------------------

## ☁️ Deployment (Streamlit Cloud)

1.  Push your project to GitHub\
2.  Go to https://streamlit.io/cloud\
3.  Click New App\
4.  Connect your GitHub repository\
5.  Select `qna_chatbot.py` as the main file\
6.  Add API keys in App Settings → Secrets

Secrets format:

GROQ_API_KEY = "your_groq_api_key"\
SERPER_API_KEY = "your_serper_api_key"

7.  Deploy 🚀

------------------------------------------------------------------------

## 🔑 Accessing Secrets in Streamlit

``` python
import streamlit as st

groq_key = st.secrets["GROQ_API_KEY"]
serper_key = st.secrets["SERPER_API_KEY"]
```

------------------------------------------------------------------------

## 🧩 How It Works

1.  User submits a query via Streamlit UI\
2.  LangChain Agent processes the query\
3.  Agent decides whether to:
    -   Respond directly using Groq LLM\
    -   Or fetch real-time information via Google Search\
4.  Response is generated and displayed\
5.  Memory maintains conversation context

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Add persistent chat history\
-   Implement RAG with custom documents\
-   Dockerize the project\
-   Deploy on AWS / Render

------------------------------------------------------------------------

## 👨‍💻 Author

Ashir Intheshar\
BSc in Computer Science

------------------------------------------------------------------------

## 📄 License

MIT License
