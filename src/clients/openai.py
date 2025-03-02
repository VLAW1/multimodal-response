import json
from typing import Any

import openai

from src.models.provider import ModelClient


class OpenAIClient(ModelClient):
    """Wrapper class to access OpenAI models."""

    def __init__(self, model: str, api_key: str) -> None:
        """
        Initialize the OpenAI client.

        Parameters
        ----------
        model : str
            Desired model to use
        api_key : str
            OpenAI API key
        """
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model

    async def generate_text(
        self,
        prompt: str,
        model: str | None = None,
        max_tokens: int = 2000,
        temperature: float = 0.5,
    ) -> str:
        """
        Generate text using OpenAI model.
        """
        model = model or self.model

        response = self.client.chat.completions.create(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        return response.choices[0].message.content.strip()

    async def generate_image(
        self,
        prompt: str,
        model: str = 'dall-e-3',
        size: str = '1024x1024',
        quality: str = 'standard',
    ) -> str:
        """
        Generate an image using DALL-E.
        """
        model = model or self.model

        response = self.client.images.generate(
            model=model,
            prompt=prompt,
            size=size,
            quality=quality,
            n=1,
        )

        return response.data[0].url

    async def generate_plan(
        self,
        prompt: str,
        model: str | None = None,
        max_tokens: int = 4000,
        temperature: float = 0.5,
    ) -> dict[str, Any]:
        """
        Generate structured plan with OpenAI.
        """
        model = model or self.model

        response = self.client.chat.completions.create(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        return json.loads(response.choices[0].message.content)
