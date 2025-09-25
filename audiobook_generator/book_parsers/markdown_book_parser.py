import logging
import re
from typing import List, Tuple

from audiobook_generator.book_parsers.base_book_parser import BaseBookParser
from audiobook_generator.config.general_config import GeneralConfig

logger = logging.getLogger(__name__)


class MarkdownBookParser(BaseBookParser):
    def __init__(self, config: GeneralConfig):
        super().__init__(config)
        if self.config.input_file:
            with open(self.config.input_file) as fobj:
                self.book = fobj.read()

    def __str__(self) -> str:
        return super().__str__()

    def validate_config(self):
        if self.config.input_file is None:
            raise ValueError("Markdown Parser: Input file cannot be empty")
        if not self.config.input_file.endswith(".md"):
            raise ValueError(f"Markdown Parser: Unsupported file format: {self.config.input_file}")

    def get_book(self):
        return self.book

    def get_book_title(self) -> str:
        return "Untitled"

    def get_book_author(self) -> str:
        return "Unknown"

    def get_chapters(self, break_string) -> List[Tuple[str, str]]:
        return [
            (str(idx), part)
            for idx, part in enumerate(self.book.split("===="))
        ]
