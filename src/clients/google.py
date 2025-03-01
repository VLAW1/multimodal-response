# import json
# from typing import Any
from src.models.provider import ModelProvider


class GoogleProvider(ModelProvider):
    """Wrapper class to access Google models."""

    def __init__(self, api_key: str | None = None, **kwargs) -> None:
        """Initialize the Google provider.

        Args:
            api_key: Google API key
            kwargs: Additional configuration options
        """
        raise NotImplementedError

    async def generate_text(
        self,
        prompt: str,
        model: str | None = None,
        max_tokens: int = 1024,
        temperature: float = 0.5,
        **kwargs,
    ) -> str:
        raise NotImplementedError

    async def generate_image(
        self,
        prompt: str,
        model: str | None = None,
        size: str = '1024x1024',
        **kwargs,
    ) -> str:
        raise NotImplementedError
