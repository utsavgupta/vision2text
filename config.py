from typing import TypedDict
from frame_iterator import FrameIterator, LocalFrameIterator, WebcamFrameIterator, VideoFrameIterator
from image_writer import ImageWriter, TempImageWriter
from llm import LLM, OpenAILLM
from document_writer import DocumentWriter, HTMLWriter
import dotenv
import os

dotenv.load_dotenv()

class Config(TypedDict):
    frame_iterator: FrameIterator
    image_writer: ImageWriter
    interval: int
    temp_image_file_name: str
    llm: LLM
    document_writer: DocumentWriter

dev: Config = {
    # "frame_iterator": WebcamFrameIterator(0),
    # "frame_iterator": LocalFrameIterator("C:\\Users\\gupta\\Code\\Gen AI\\vision2text\\images"),
    "frame_iterator": VideoFrameIterator("./waucissa.mov"),
    "image_writer": TempImageWriter(),
    "interval": 15,
    "temp_image_file_path": "C:\\Users\\gupta\\Code\\Gen AI\\vision2text\\tmp.jpeg",
    "llm": OpenAILLM(os.environ['OPENAI_API_KEY']),
    "document_writer": HTMLWriter("C:\\Users\\gupta\\Code\\Gen AI\\vision2text", "C:\\Users\\gupta\\Code\\Gen AI\\vision2text\\dashboard.html")
} 
