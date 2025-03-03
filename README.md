# Multimodal Response

## Overview

This project generates a response in a text-to-text-and-image fashion where the response to a user prompt uses both text and images through an orchestrated workflow.
The Task Planner plans responses and coordinates between text and image generators, allowing for interleaved text and image outputs.

## Example

On prompt:

> Explain the impact of quantum computing on modern cryptography. Include diagrams showing how quantum algorithms like Shor's algorithm can break RSA encryption. Compare the timeline of quantum computing development with the evolution of post-quantum cryptographic methods. End with a visual representation of which current encryption methods are most vulnerable to quantum attacks.

Response shown in `example-response.md`.

## How It Works

The responses are generated as follows:

- A Task Planner is asked to generate a list of tasks for text and image elements to compose a response, along with a prompt for each element.
- Optionally, each subtask prompt is refined via another round of LLM calls.
- With the subtasks, a Task Manager passes the subtask prompts to the respective text/image generation clients.
- Finally, the individual text and image elements are sewn together to create the final response, and saved to a `.md` and/or `.html` file.

## Setup Instructions

1. Clone the repository and `cd` into it:
   ``` sh
   git clone https://github.com/VLAW1/multimodal-response.git
   cd multimodal-response
   ```

2. Create a virtual environment and install the required dependencies:
   ``` sh
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Create a `.env`
   ``` sh
   touch .env
   ```

4. Add your API keys:
   ``` sh
   ANTHROPIC_API_KEY="your-anthropic-key"
   OPENAI_API_KEY="your-openai-key"
   GOOGLE_API_KEY="your-google-key"
   ```

5. Configure the providers, models, and parameters in `setup.py` (a default setup is already provided).

4. Start it with:
   ``` sh
   python3 -m src
   ```

5. Enter your prompt when asked, and wait for the output.

Your response will be saved as `response.md` (or `response.html` if you switch the save function in `setup.py`).
You can also view some intermediate outputs in the `app.log` files that will be generated.

<!-- ## To Do -->

## License
This project is licensed under the MIT License.