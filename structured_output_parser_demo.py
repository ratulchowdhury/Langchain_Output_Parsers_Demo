from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
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

schema = [
    ResponseSchema(name="gameplay", description="a brief summary of the topic"),
    ResponseSchema(name="advantages", description="the advantages of the topic, with examples of where it has been executed impeccably."),
    ResponseSchema(name="tactical_flaws", description="the flaws of the topic, with examples of where the system has collapsed.")
]
parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(template="""Consider yourself a football pundit. Now your task is to generate a summary, advantages, flaws of the following {topic}, \n {format_instructions}""",
                           input_variables = ["topic"],
                           partial_variables ={"format_instructions":parser.get_format_instructions()})

chain = template | llm| parser
topic_name  = "catenaccio style of defense."
result = chain.invoke({"topic":topic_name})
print("Type of the output :", type(result))
print("Output :", result)
print(f"Gameplay of the {topic_name}:",result["gameplay"])
print(f"Advantages of the {topic_name}:",result["advantages"])
print(f"Flaws of the {topic_name}:",result["tactical_flaws"])