import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPEN_ROUTER_API_KEY"))

def ask_tutor(user_query, context):
    prompt = f"""
    You are a curriculum-aligned tutor for students in Africa.
    Use the following curriculum context to answer the student's question accurately.
    If the answer isn't in the context, use your general knowledge but mention that it's supplementary.

    Context: {context[:3000]} # Simple truncation for the pilot
    Student's Question: {user_query}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content