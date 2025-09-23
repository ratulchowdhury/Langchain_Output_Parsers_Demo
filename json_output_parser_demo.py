from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import JsonOutputParser  
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

parser = JsonOutputParser()
template = PromptTemplate(template="""Consider yourself a football pundit. Now your task is to generate a summary, advantages, flaws of the following {topic}, \n {format_instructions}""",
                           input_variables = ["topic"],
                           partial_variables ={"format_instructions":parser.get_format_instructions()})

chain = template | llm| parser
topic_name  = "catenaccio style of defense."
result = chain.invoke({"topic":topic_name})
print("Type of the output :", type(result))
print(f"Summary of the {topic_name}:",result["summary"])
print(f"Advantages of the {topic_name}:",result["advantages"])
print(f"Flaws of the {topic_name}:",result["flaws"])