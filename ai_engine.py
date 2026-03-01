from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def explain_clause_ai(clause, risk):

    try:

        prompt = f"""
You are a contract risk analyst.

Explain WHY this clause received this risk level.

Rules:
- Maximum 3 bullet points
- Very simple English
- Mention only risks visible in clause
- No assumptions

Risk Level: {risk}

Clause:
{clause}
"""

        response = client.chat.completions.create(

            model="deepseek/deepseek-chat",

            messages=[
                {"role": "user", "content": prompt}
            ],

            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception:

        return "• AI analysis unavailable."