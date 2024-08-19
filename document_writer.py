import abc
from model import ExtractedText
from jinja2.loaders import FileSystemLoader
from jinja2 import Template, Environment

class DocumentWriter(abc.ABC):

    @abc.abstractmethod
    async def execute(self, extracted_text: ExtractedText):
        pass

class HTMLWriter(DocumentWriter):

    def __init__(self, template_path: str, output_path: str):
        template_loader = FileSystemLoader(searchpath=template_path)
        template_env = Environment(loader=template_loader)
        self.__template: Template = template_env.get_template("template.jinja")
        self.__output_path: str = output_path

    async def execute(self, extracted_text: ExtractedText):
        
        content = self.__template.render(goals=extracted_text.goals, achievements=extracted_text.achievements, feedback=extracted_text.feedback)

        with open(self.__output_path, "w") as f:
            f.write(content)