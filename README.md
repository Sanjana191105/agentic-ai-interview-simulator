# 🎯 AI Interview Simulator

## 📌 Project Description
This project simulates a real-time technical interview using Generative AI.  
It dynamically generates interview questions based on the selected role and evaluates user responses with feedback and scoring.

## 🚀 Features
- Dynamic interview question generation (Beginner → Advanced)
- Answer evaluation with score and feedback
- Weak area analysis
- HR interview round simulation
- Agent-based architecture using LangChain

## 🛠️ Technologies Used
- Python
- LangChain
- Google Gemini API (LLM)

## 🧠 How It Works
1. User selects a role (Frontend / Java / Data Science)
2. System generates 3 interview questions
3. User answers each question
4. AI evaluates answers and provides:
   - Score
   - Feedback
   - Improvement tips
5. System analyzes weak areas
6. HR round question is generated and evaluated

## ▶️ How to Run

1. Install dependencies:
   pip install langchain langchain-google-genai

2. Run the program:
   python main.py

3. Enter your Google API Key when prompted

## 🔐 Security Note
API key is not hardcoded for security reasons.  
Users must enter their own API key at runtime.

## 🎯 Use Case
This system helps students:
- Practice interviews
- Improve answering skills
- Identify weak areas
- Build confidence for real interviews


## 📈 Future Enhancements
- Web-based UI (Streamlit)
- Database for storing performance history
- Multi-role interview simulation
- Advanced scoring analytics

## 👩‍💻 Author
Sanjana S
B.E Computer Science Engineering

## ⭐ Conclusion
This project demonstrates the use of Agentic AI and Large Language Models to create an intelligent and interactive interview preparation system.
