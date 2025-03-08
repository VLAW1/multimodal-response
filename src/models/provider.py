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
        """
        Generate text from a prompt.

        Parameters
        ----------
        prompt : str
            The text prompt
        model : str | None, optional
            Model name to use (provider-specific), by default None
        max_tokens : int, optional
            Maximum number of tokens to generate, by default 2000
        temperature : float, optional
            Sampling temperature, by default 0.5

        Returns
        -------
        str
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
        """
        Generate an image from a prompt.

        Parameters
        ----------
        prompt : str
            Description of the image to generate
        model : str | None, optional
            Model name to use (provider-specific), by default None
        size : str, optional
            Size specification for the image, by default '1024x1024'
        quality : str, optional
            Quality specificiation for the image, by default 'standard'

        Returns
        -------
        str
            URL of the generated image
        """
        pass

    @abstractmethod
    async def generate_tikz(
        self,
        prompt: str,
        model: str | None = None,
        max_tokens: int = 2000,
        temperature: float = 0.5,
    ) -> str:
        """
        Generate TikZ code from a prompt.

        Parameters
        ----------
        prompt : str
            Description of the diagram to generate
        model : str | None, optional
            Model name to use (provider-specific), by default None
        max_tokens : int, optional
            Maximum number of tokens to generate, by default 2000
        temperature : float, optional
            Sampling temperature, by default 0.5

        Returns
        -------
        str
            Generated TikZ code
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

        Parameters
        ----------
        prompt : str
            Description of the diagram to generate
        model : str | None, optional
            Model name to use (provider-specific), by default None
        max_tokens : int, optional
            Maximum number of tokens to generate, by default 2000
        temperature : float, optional
            Sampling temperature, by default 0.5

        Returns
        -------
        dict[str, Any]
            Generated plan (in JSON format)
        """
        pass

    @classmethod
    def create_client(
        cls,
        provider: ModelProvider,
        model: str,
        api_key: str,
    ) -> 'ModelClient':
        """
        Factory method to create a client instance.

        Parameters
        ----------
        provider : ModelProvider
            Type of client to create
        model : str
            Model to use (provider-specific)
        api_key : str
            API key for the provider

        Returns
        -------
        ModelClient
            A ModelClient instance

        Raises
        ------
        ValueError
            In case of unknown provider type
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
