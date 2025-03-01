from typing import Any
from enum import StrEnum

from pydantic import BaseModel, Field


class ElementType(StrEnum):
    TEXT = 'text'
    IMAGE = 'image'


class TextElement(BaseModel):
    type: ElementType = ElementType.TEXT
    content: str


class ImageElement(BaseModel):
    type: ElementType = ElementType.IMAGE
    url: str
    alt_text: str | None = None
    caption: str | None = None


type ResponseElement = TextElement | ImageElement


class MultimodalResponse(BaseModel):
    elements: list[ResponseElement] = Field(default_factory=list)

    def add_text(self, text: str) -> None:
        """Add a text element to the response."""
        self.elements.append(TextElement(content=text))

    def add_image(
        self,
        url: str,
        alt_text: str | None = None,
        caption: str | None = None,
    ) -> None:
        """Add an image element to the response."""
        self.elements.append(
            ImageElement(url=url, alt_text=alt_text, caption=caption)
        )

    def add_element(self, type: str, content: Any) -> None:
        if type == 'text':
            self.add_text(content)
        elif type == 'image':
            self.add_image(**content)

    def to_markdown(self) -> str:
        """Convert the multimodal response to markdown format."""
        md = ''
        for element in self.elements:
            if element.type == ElementType.TEXT:
                md += f'{element.content}\n\n'
            elif element.type == ElementType.IMAGE:
                alt = element.alt_text or 'Generated image'
                md += f'![{alt}]({element.url})\n'
                if element.caption:
                    md += f'*{element.caption}*\n'
                md += '\n'
        return md.strip()
