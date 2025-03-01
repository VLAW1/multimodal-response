from abc import ABC, abstractmethod
from enum import StrEnum
from typing import Any

# from pydantic import BaseModel


class ModelProvider(StrEnum):
    OPENAI = 'openai'
    ANTHROPIC = 'anthropic'
    GOOGLE = 'google'


class ModelClient(ABC):
    """Base class for model client calls."""

    @abstractmethod
    async def generate_text(
        self,
        prompt: str,
        model: str | None = None,
        max_tokens: int = 2000,
        temperature: float = 0.5,
    ) -> str:
        """Generate text from a prompt.

        Args:
            prompt: The text prompt
            model: Model name to use (provider-specific)
            max_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            kwargs: Additional provider-specific parameters

        Returns:
            Generated text
        """
        pass

    @abstractmethod
    async def generate_image(
        self,
        prompt: str,
        model: str | None = None,
        size: str = '1024x1024',
        quality: str = 'standard',
    ) -> str:
        """Generate an image from a prompt.

        Args:
            prompt: Description of the image to generate
            model: Model name to use (provider-specific)
            size: Size specification for the image
            kwargs: Additional provider-specific parameters

        Returns:
            URL of the generated image
        """
        pass

    @abstractmethod
    async def generate_plan(
        self,
        prompt: str,
        model: str | None = None,
        max_tokens: int = 4000,
        temperature: float = 0.5,
    ) -> dict[str, Any]:
        """
        Generate structured plan.
        """
        pass

    @classmethod
    def create_client(
        cls,
        provider: ModelProvider,
        model: str,
        api_key: str,
    ) -> 'ModelClient':
        """Factory method to create a client instance.

        Args:
            provider: Type of client to create
            api_key: API key for the provider

        Returns:
            A ModelClient instance
        """
        if provider == ModelProvider.OPENAI:
            from src.clients.openai import OpenAIClient

            return OpenAIClient(model=model, api_key=api_key)
        elif provider == ModelProvider.ANTHROPIC:
            from src.clients.anthropic import AnthropicClient

            return AnthropicClient(model=model, api_key=api_key)
        # elif provider_type == ModelProvider.GOOGLE:
        #     from .google import GoogleProvider

        #     return GoogleProvider(api_key=api_key)
        else:
            raise ValueError(f'Unknown provider: {provider}')
