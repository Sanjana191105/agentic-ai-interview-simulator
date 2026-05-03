import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

# Secure API input
os.environ["GOOGLE_API_KEY"] = input("Enter your API key: ")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

def generate_questions(role):
    return llm.invoke(f"""
    Generate 3 interview questions for {role} role.
    Make them beginner, intermediate, advanced.
    """).content

def evaluate_answer(answer):
    return llm.invoke(f"""
    Evaluate this answer:

    {answer}

    Give output in this format:
    Score: x/10
    Feedback:
    Improvement:
    """).content

def hr_question(_):
    return llm.invoke("Ask one HR interview question").content

tools = [
    Tool(name="Question Generator", func=generate_questions, description="Generate questions"),
    Tool(name="Answer Evaluator", func=evaluate_answer, description="Evaluate answers"),
    Tool(name="HR Question", func=hr_question, description="HR questions")
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

print("🎯 AI Interview Simulator Started\n")

role = input("Enter role: ")

questions = generate_questions(role)
print("\n📌 Questions:\n", questions)

answers = []

for i in range(3):
    ans = input(f"\nYour Answer {i+1}: ")
    answers.append(ans)

    print("\n📊 Evaluation:\n", evaluate_answer(ans))

combined_answers = " ".join(answers)

weak = llm.invoke(f"""
Analyze these answers:
{combined_answers}
Tell weak areas.
""").content

print("\n📉 Weak Areas:\n", weak)

print("\n--- 💼 HR ROUND ---")

hr_q = hr_question("")
print("\nHR Question:", hr_q)

hr_ans = input("\nYour HR Answer: ")

print("\n📊 HR Evaluation:\n", evaluate_answer(hr_ans))
