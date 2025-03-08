import json
from typing import Any

import anthropic

from src.models.provider import ModelClient


class AnthropicClient(ModelClient):
    """Wrapper class to access Anthropic models."""

    def __init__(self, model: str, api_key: str) -> None:
        """
        Initialize the client.

        Parameters
        ----------
        model : str
            Desired model to use
        api_key : str
            Anthropic API key
        """
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model

    async def generate_text(
        self,
        prompt: str,
        model: str | None = None,
        max_tokens: int = 2000,
        temperature: float = 0.5,
    ) -> str:
        """
        Generate text element with Claude.
        """
        model = model or self.model

        response = self.client.messages.create(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        return response.content[0].text

    async def generate_image(
        self,
        prompt: str,
        model: str | None = None,
        size: str = '1024x1024',
        quality: str = 'standard',
    ) -> str:
        raise NotImplementedError(
            'Anthropic/Claude does not support image generation.'
        )

    async def generate_tikz(
        self,
        prompt: str,
        model: str | None = None,
        max_tokens: int = 2000,
        temperature: float = 0.5,
    ) -> str:
        """
        Generate TikZ code with Claude.
        """
        model = model or self.model

        response = self.client.messages.create(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        tikz_code = response.content[0].text

        # Clean up the response to extract just the TikZ code
        if '\\begin{tikzpicture}' in tikz_code:
            tikz_code = tikz_code.split('\\begin{tikzpicture}')[1]
        if '\\end{tikzpicture}' in tikz_code:
            tikz_code = tikz_code.split('\\end{tikzpicture}')[0]

        return f'\\begin{{tikzpicture}}\n{tikz_code.strip()}\n\\end{{tikzpicture}}'

    async def generate_plan(
        self,
        prompt: str,
        model: str | None = None,
        max_tokens: int = 4000,
        temperature: float = 0.5,
        use_extended_thinking: bool = False,
    ) -> dict[str, Any]:
        """
        Generate structured plan with Claude.
        """
        model = model or self.model

        if use_extended_thinking and model == 'claude-3-7-sonnet-20250219':
            response = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                thinking={'type': 'enabled', 'budget_tokens': 2048},
                messages=[{'role': 'user', 'content': prompt}],
                temperature=temperature,
            )
        else:
            response = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                messages=[{'role': 'user', 'content': prompt}],
                temperature=temperature,
            )
        return json.loads(response.content[0].text)
