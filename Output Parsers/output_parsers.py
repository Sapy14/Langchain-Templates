from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

template1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt1=template1.invoke({'topic':'LLM'})
result=model.invoke(prompt1)
print(result.content)

