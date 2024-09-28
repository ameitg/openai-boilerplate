import openai
from dotenv import load_dotenv
load_dotenv()
import os
from getTextFromUrl import getTextFromUrl
openai.api_key = os.getenv("OPENAI_API_KEY")


# Function to load the text and pass it to the model
def getAnswerFrontext(text, question):
    # Prepare prompt with text content
    prompt = f"""
    You are provided with the following text:
    '{text}'
    
    Based on this text, answer the following question: {question}
    """
    
    # Use OpenAI's completion API to get an answer based on the text
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # You can use "gpt-3.5-turbo" if needed
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # Return the answer
    return response
webpage_text = getTextFromUrl("https://profile.amitg.pro")
answer = getAnswerFrontext(webpage_text, "Show skills related to Technical project manager  with employer name")

print("Answer:", answer)
