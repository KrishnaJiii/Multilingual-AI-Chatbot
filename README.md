# 🌍 Multilingual AI Chatbot

A **Streamlit-based Multilingual AI Chatbot** powered by **Groq LLM (LLaMA 3.3 70B)** with real-time streaming responses.  
The chatbot supports multiple languages and securely handles API keys for safe deployment.

---

## 🚀 Live Demo

🔗 **Live App:**  
[**Click here to launch the Streamlit App**](https://multilingual-ai-chatbot-by-krishna-bedi.streamlit.app)
---

## 📌 Features

- 🌐 Multilingual support (English, Hindi, Spanish, French, etc.)
- ⚡ Word-by-word streaming responses
- 💬 Chat history management
- 🔐 Secure API key handling using environment variables
- ☁️ Easy deployment on Streamlit Cloud

---

## 🧠 Tech Stack

- **Python**
- **Streamlit**
- **Groq API**
- **LLaMA 3.3 70B**
- **dotenv**
- **GitHub + Streamlit Cloud**

---

## 📂 Project Structure
```bash
Multilingual-AI-Chatbot/
│
├── app.py # Streamlit UI and chat handling
├── chatbot.py # Groq API & chatbot logic
├── requirements.txt # Dependencies
├── .gitignore # Ignored files
└── README.md # Project documentation
```

---

## ▶️ Run Locally

Follow these steps to run the Multilingual AI Chatbot on your local machine.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/KrishnaJiii/Multilingual-AI-Chatbot.git
cd Multilingual-AI-Chatbot
```


### 2️⃣ Create & Activate Virtual Environment (Recommended)

Windows
```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```


### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```


### 4️⃣ Set Up Environment Variables

Create a .env file in the root directory and add:
```bash
GROQ_API_KEY=your_groq_api_key_here
```


### 5️⃣ Run the Application
```bash
streamlit run app.py
```

### 6️⃣ Open in Browser

Once started, open:
```bash
http://localhost:8501
```

---

## 🧠 Key Learnings

- Learned how to build an end-to-end Generative AI application using Streamlit and LLM APIs.

- Implemented secure API key management using environment variables and Streamlit Secrets.

- Gained hands-on experience with Groq LLMs (LLaMA 3.3 70B) for real-time AI responses.

- Implemented word-by-word streaming to improve user experience and responsiveness.

- Designed a multi-chat session system using Streamlit session state.

- Understood GitHub-based deployment workflows and cloud hosting using Streamlit Cloud.

- Improved debugging skills by resolving common Python and Streamlit errors.

- Learned best practices for production-ready AI apps, including code structure and security.

---

## 🔐 Security

- API keys are never hardcoded in the source code
- Sensitive credentials are stored using environment variables
- `.env` file is ignored using `.gitignore`
- Streamlit Secrets are used for cloud deployment

---

## 👤 Author

**Krishna Bedi**  
Data Science & Generative AI Enthusiast

- GitHub: https://github.com/KrishnaJiii
- LinkedIn: https://www.linkedin.com/in/krishna-bediofficial/

---

⭐ If you found this project useful, feel free to star the repository!
