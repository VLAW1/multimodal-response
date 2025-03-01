import os
import logging

from dotenv import load_dotenv

from src.models.provider import ModelProvider, ModelClient
from src.orchestration.task_planner import TaskPlanner
from src.orchestration.task_manager import TaskManager
from src.utils.formatting import (
    save_response_to_html,  # noqa: F401
    save_response_to_markdown,  # noqa: F401
)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.FileHandler('app.log'))


async def respond():
    load_dotenv()

    # Create clients for each component
    task_planner = TaskPlanner(
        provider=ModelProvider.ANTHROPIC,
        api_key=os.getenv('ANTHROPIC_API_KEY'),
        model='claude-3-7-sonnet-20250219',
        use_extended_thinking=True,
    )
    text_element_client = ModelClient.create_client(
        provider=ModelProvider.ANTHROPIC,
        model='claude-3-7-sonnet-20250219',
        api_key=os.getenv('ANTHROPIC_API_KEY'),
    )
    image_element_client = ModelClient.create_client(
        provider=ModelProvider.OPENAI,
        model='dall-e-3',
        api_key=os.getenv('OPENAI_API_KEY'),
    )

    # Initialize the task manager
    task_manager = TaskManager(
        text_element_client=text_element_client,
        image_element_client=image_element_client,
        task_planner=task_planner,
        refine_tasks=True,
    )

    # Get user input
    user_prompt = input('Enter your prompt for a multimodal response: ')

    print('\nPlanning and generating response...')
    response = await task_manager.generate_response(user_prompt)

    # Display the response in markdown format
    print('\nGenerated Response (Markdown):')
    print('-----------------------------')
    print(response.to_markdown())
    print('-----------------------------')

    # Save response
    save_response_to_markdown(response, 'response.md', 'Multimodal Response')
    # save_response_to_html(response, 'response.html', 'Multimodal Response')
