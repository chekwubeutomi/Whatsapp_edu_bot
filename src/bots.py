import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",  # NO trailing slash here
    api_key=os.getenv("OPEN_ROUTER_API_KEY"),
    default_headers={
        "HTTP-Referer": "http://localhost:5000", # Required for some free models
        "X-Title": "EduBot_Pilot",
    }
)




def ask_tutor(user_query, context):
    prompt = f"""
    You are a curriculum-aligned tutor for students in Africa.
    Use the following curriculum context to answer the student's question accurately.
    If the answer isn't in the context, use your general knowledge but mention that it's supplementary.

    Context: {context[:3000]} # Simple truncation for the pilot
    Student's Question: {user_query}
    """

    try:
        response = client.chat.completions.create(
            model="openrouter/auto",
            messages=[{"role": "user", "content": prompt}]
        )

        if hasattr(response, "choices") and len(response.choices) > 0:
            return response.choices[0].message.content
        else:
            return str(response)
    except Exception as e:
        return "Sorry, I encountered an error while processing your request."

