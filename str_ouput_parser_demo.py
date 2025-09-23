from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os 
load_dotenv()

hf_token = os.getenv("HUGGINGFACE_API_KEY")

llm = HuggingFaceEndpoint(
    endpoint_url="Qwen/Qwen3-Next-80B-A3B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
)

llm = ChatHuggingFace(llm=llm, temperature = 0.5)

template1 = PromptTemplate(template="""Consider yourself a football pundit. Now write an essay about the following {topic}""", 
                           input_variables=["topic"])

template2 = PromptTemplate(template="""Consider yourself a text summarizer. Now summarize the following {text} in 5 lines.""", 
                           input_variables=["text"])

parser = StrOutputParser()

chain = template1 | llm | parser| template2 | llm | parser

result = chain.invoke({"topic": "3-5-2 formation."})

print(result)