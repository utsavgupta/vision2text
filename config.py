from typing import TypedDict
from frame_iterator import FrameIterator, LocalFrameIterator
from image_writer import ImageWriter, TempImageWriter
from llm import LLM, OpenAILLM
from document_writer import DocumentWriter, HTMLWriter

class Config(TypedDict):
    frame_iterator: FrameIterator
    image_writer: ImageWriter
    interval: int
    temp_image_file_name: str
    llm: LLM
    document_writer: DocumentWriter

dev: Config = {
    "frame_iterator": LocalFrameIterator(".\\images"),
    "image_writer": TempImageWriter(),
    "interval": 15,
    "temp_image_file_path": ".\\tmp.jpeg",
    "llm": OpenAILLM(""),
    "document_writer": HTMLWriter(".\\", ".\\dashboard.html")
} 
