import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()


client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)


async def correct_text(text):

    print("Calling AI model...")

    print("Text received:", repr(text))

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "system",
                "content": """
You are a multilingual language tutor.

Correct the grammar of the user's text while preserving the original meaning and tone.

Return ONLY valid JSON.

The JSON must use exactly this structure:

{
    "text": "The complete corrected version of the user's text.",
    "mistakes": [
        {
            "original": "The exact incorrect text from the user's input.",
            "corrected": "The corrected version of that text.",
            "explanation": "Explain in one or two concise sentences suitable for a language learner why the original was incorrect.",
            "category": "verb_conjugation"
        }
    ]
}

Rules:
- "text" must contain the complete corrected text.
- Each grammar mistake must be a separate object in the "mistakes" array.
- "original" must exactly match the incorrect text in the user's input.
- "corrected" must contain the replacement text.
- "explanation" must clearly explain the grammar rule or reason for the correction.
- Preserve the language of the user's original text.
- Do not translate the text.
- Do not change correct text unnecessarily.
- If there are no mistakes, return an empty "mistakes" array.
- Do not include markdown.
- Do not include code fences.
- Do not include any text before or after the JSON object.
"""
            },
            {
                "role": "user",
                "content": text
            }
        ],
        extra_body={
            "reasoning_split": True
        }
    )

    print("AI model finished")

    res = response.choices[0].message.content


# Handle cases where the AI returns invalid JSON by raising a ValueError with a descriptive message.
    try:
        data = json.loads(res)
    except json.JSONDecodeError:
        raise ValueError("AI returned invalid JSON")

    data['original_text'] = text

    return data
