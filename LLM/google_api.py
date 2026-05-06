from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=GoogleGenerativeAI(model='gemini-2.5-flash')
result=model.invoke("What is capital of India")
print(result)