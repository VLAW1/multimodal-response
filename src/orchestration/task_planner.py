import logging
from typing import Any

from src.orchestration.prompts.planning_prompt import planning_prompt_template
from src.orchestration.prompts.planning_examples import (
    query_example,
    task_response_example,
)
from src.models.provider import ModelProvider, ModelClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.FileHandler('app.log'))


class TaskPlanner:
    """Plans the subtasks needed for a multimodal response."""

    def __init__(
        self,
        provider: ModelProvider,
        api_key: str,
        model: str,
        use_extended_thinking: bool = False,
        max_tokens: int = 4000,
        temperature: float = 0.5,
    ) -> None:
        """
        Initialize the task planner.

        Parameters
        ----------
        provider : ModelProvider
            The provider to use
        api_key : str
            Provider API key
        model : str
            The model to use (provider-specific)
        """
        self.provider = provider
        self.model = model
        self.client = ModelClient.create_client(
            self.provider, model=self.model, api_key=api_key
        )
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.use_extended_thinking = use_extended_thinking

    async def generate_plan(self, prompt: str) -> list[dict[str, Any]]:
        """Generate a plan of subtasks for responding to the given prompt.

        Args:
            prompt: The initial user prompt

        Returns:
            A list of subtasks with their details
        """
        planning_prompt = planning_prompt_template.format(
            query_example=query_example,
            task_response_example=task_response_example,
            prompt=prompt,
        )
        log.info(f'Planning prompt: {planning_prompt}')

        plan = await self.client.generate_plan(
            prompt=planning_prompt,
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        log.info(f'Generated plan: {plan}')

        return plan['subtasks']
