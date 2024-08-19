import abc
from cv2 import imwrite, Mat

class ImageWriter(abc.ABC):

    @abc.abstractmethod
    async def write(self, abs_file_path: str, frame: Mat):
        pass

class TempImageWriter(ImageWriter):

    def __init__(self):
        pass        

    async def write(self, abs_file_path: str, frame: Mat):
        
        imwrite(abs_file_path, frame)
        