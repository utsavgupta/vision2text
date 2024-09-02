from config import Config
from frame_iterator import FrameIterator
from image_writer import ImageWriter
from llm import LLM
from document_writer import DocumentWriter
import asyncio
import logging

class Vision2TextEngine:

    logger = logging.getLogger(__name__)

    def __init__(self, config: Config):
        self.__runnable: bool = True
        self.__frame_iterator: FrameIterator = config.get("frame_iterator")
        self.__image_writer: ImageWriter = config.get("image_writer")
        self.__temp_image_file_path = config.get("temp_image_file_path")
        self.__interval: int = config.get("interval")
        self.__llm: LLM = config.get("llm")
        self.__document_writer = config.get("document_writer")

    async def run(self):
        try:
            await self.__run()
        except asyncio.CancelledError as e:
            self.logger.info("Stopping")
            await self.stop()
            await asyncio.sleep(3)
            self.logger.info("Bye!")

        
    async def __run(self):

        for frame in self.__frame_iterator:

            if not self.__runnable:
                break
            
            await self.__image_writer.write(self.__temp_image_file_path, frame)

            # try:
            #     extracted_text = await self.__llm.extract_text(self.__temp_image_file_path)
            # except Exception as e:
            #     self.logger.error(f"Cannot extract text from image: {e}")
            #     continue

            # await self.__document_writer.execute(extracted_text)

            await asyncio.sleep(self.__interval)

        self.__frame_iterator.shutdown()

    async def stop(self):
        
        self.__runnable = False