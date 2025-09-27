from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
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

class outputSchema(BaseModel):
    gameplay :str = Field(description="a brief summary of the topic")
    advantages :str = Field(description="the advantages of the topic, with examples of where it has been executed impeccably.")
    tactical_flaws :str = Field(description="the flaws of the topic, with examples of where the system has collapsed.")
    overall_rating :int = Field(gt = 0, lt = 10, description="Overall rating of the topic on a scale of 1 to 10")
    
parser = PydanticOutputParser(pydantic_object=outputSchema)
template = PromptTemplate(template="""Consider yourself a football pundit. Now your task is to generate a summary, advantages, flaws of the following {topic}, \n {format_instructions}""",
                           input_variables = ["topic"],
                           partial_variables ={"format_instructions":parser.get_format_instructions()})

chain = template | llm| parser
topic_name  = "catenaccio style of defense"
result = chain.invoke({"topic":topic_name})
print("Type of the output :", type(result))
print("Output :", result)
print(f"Gameplay of the {topic_name}:",result.gameplay)
print(f"Advantages of the {topic_name}:",result.advantages)
print(f"Flaws of the {topic_name}:",result.tactical_flaws)
print(f"Overall rating of the {topic_name}:",result.overall_rating)