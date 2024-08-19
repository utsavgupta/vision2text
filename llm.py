from langchain_openai import ChatOpenAI 
import abc
from model import ExtractedText
from langchain_core.prompts import HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
import base64

class LLM(abc.ABC):

    async def extract_text(self, image_abs_path: str) -> ExtractedText:
        pass

class OpenAILLM(LLM):
    
    def __init__(self, api_key: str):
        self.__llm: ChatOpenAI = ChatOpenAI(api_key=api_key, model="gpt-4o")
        self.__parser: PydanticOutputParser = PydanticOutputParser(pydantic_object=ExtractedText)

        self.__system_prompt_tpl: SystemMessagePromptTemplate = SystemMessagePromptTemplate.from_template(
            'You will receive pictures of a white sheet of paper with sticky notes on it. A note can be yellow, pink, or peach. The yellow notes contain a goal, the pink notes contain an achievement, and the peach notes contain a feedback. You will be given images, your task is to extract lists of goals, achievements, and feedback from the images.\n{format_instructions}',
            partial_variables={"format_instructions": self.__parser.get_format_instructions()}
        )

        self.__user_prompt_tpl: HumanMessagePromptTemplate = HumanMessagePromptTemplate.from_template(
            [
                {
                    "image_url": 'data:image/jpeg;base64,{encoded_image}'
                }
            ]
        )

    async def extract_text(self, image_abs_path: str) -> ExtractedText:

        messages = [
            self.__system_prompt_tpl.format(),
            self.__user_prompt_tpl.format(encoded_image=await self.__load_and_encode_image(image_abs_path))
        ]

        response = await self.__llm.ainvoke(messages)

        extracted_text = await self.__parser.aparse(response.content)

        return extracted_text

    async def __load_and_encode_image(self, image_abs_path: str) -> str:
        
        encoded_image = ""

        with open(image_abs_path, "rb") as f:
            encoded_image = base64.b64encode(f.read()).decode("utf-8")

        return encoded_image
    