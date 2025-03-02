import json
from typing import Any
from io import BytesIO

from google import genai
from google.genai import types
from PIL import Image

from src.models.provider import ModelClient


class GoogleClient(ModelClient):
    """Wrapper class to access Google models."""

    def __init__(self, model: str, api_key: str) -> None:
        """
        Initialize the client.

        Parameters
        ----------
        model : str
            Desired model to use
        api_key : str
            Google API key
        """
        self.client = genai.Client(api_key=api_key)
        self.model = model

    async def generate_text(
        self,
        prompt: str,
        model: str | None = None,
        max_tokens: int = 1024,
        temperature: float = 0.5,
    ) -> str:
        """
        Generate text.
        """
        model = model or self.model

        response = self.client.models.generate_content(
            model=model,
            contents=[prompt],
            config=types.GenerateContentConfig(
                max_output_tokens=max_tokens,
                temperature=temperature,
            ),
        )

        return response.text

    async def generate_image(
        self,
        prompt: str,
        model: str = 'imagen-3.0-generate-002',
        # size: str = '1024x1024',
    ) -> str:
        """
        Generate an image using Imagen.
        """
        response = self.client.models.generate_images(
            model=model,
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
            ),
        )

        image = Image.open(
            BytesIO(response.generated_images[0].image.image_bytes)
        )
        return image

    async def generate_plan(
        self,
        prompt: str,
        model: str | None = None,
        max_tokens: int = 4000,
        temperature: float = 0.5,
    ) -> dict[str, Any]:
        """
        Generate structured plan with Gemini.
        """
        model = model or self.model

        response = self.client.models.generate_content(
            model=model,
            contents=[prompt],
            config=types.GenerateContentConfig(
                max_output_tokens=max_tokens,
                temperature=temperature,
            ),
        )

        return json.loads(response.text)
