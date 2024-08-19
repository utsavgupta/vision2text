import abc
import os
from typing import List
import cv2

class FrameIterator(abc.ABC):
    
    @abc.abstractmethod
    def __iter__(self):
        pass

    @abc.abstractmethod
    def __next__(self):
        pass

    @abc.abstractmethod
    def shutdown(self):
        pass


class LocalFrameIterator(FrameIterator):

    def __init__(self, path: str):
        
        self.__image_file_names = self.__get_file_list(path)
        self.__pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        
        if self.__pos >= len(self.__image_file_names):
            raise StopIteration
        
        img = cv2.imread(self.__image_file_names[self.__pos])

        self.__pos += 1

        return img

    def __get_file_list(self, path: str) -> List[str]:

        files = []

        for file_name in os.listdir(path):

            abs_filepath = os.path.abspath(os.path.join(path, file_name))

            if os.path.isfile(abs_filepath) and abs_filepath.endswith(".jpeg"):
                files.append(abs_filepath)

        files = sorted(files)

        return files
    
    def shutdown(self):
        pass

class WebcamFrameIterator(FrameIterator):
    pass