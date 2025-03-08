refine_text_task_template = (
    'As an expert prompt engineer, improve the following text generation'
    ' prompt to produce better results. '
    'Your prompt will be used to generate a text section for an individual '
    ' text element as part of a larger response to the user prompt shown'
    ' below. '
    'You can think of this as a section in a report.'
    '\n\n'
    'Original user query: {user_prompt}'
    '\n\n'
    'Current text prompt to refine: {task_prompt}'
    '\n\n'
    'Improve the prompt by:\n'
    '1. Making it more specific and detailed\n'
    '2. Adding necessary context to maintain flow with surrounding elements\n'
    '3. Specifying desired tone, style, and length\n'
    '4. Highlighting key points that should be addressed\n'
    '5. Including any necessary instructions about how to structure the text'
    '\n\n'
    'Remember, this text is one element of a larger response. The task is'
    ' only to improve the text generation prompt, NOT write a prompt to answer'
    ' the user directly.\n'
    'Provide ONLY the enhanced prompt text with no additional explanation or'
    ' commentary.\n'
    'Ensure the enhanced prompt maintains the original intent but adds'
    ' precision and clarity.\n'
)

refine_image_task_template = (
    'As an expert prompt engineer for image generation, improve the following'
    ' image prompt to produce better results. '
    'Your prompt will be used to generate an image for an individual figure in'
    ' a multimodal response to the user prompt shown below. '
    'You can think of this as a figure within a journal article.'
    '\n\n'
    'Original user query: {user_prompt}'
    '\n\n'
    'Current image prompt to refine: {task_prompt}'
    '\n\n'
    'Improve the prompt by:\n'
    '1. Adding vivid visual details and specificity\n'
    '2. Specifying composition, perspective, and style\n'
    '3. Including art direction (lighting, colors, mood)\n'
    '4. Clarifying what elements should be emphasized\n'
    '5. Ensuring the image will complement surrounding text elements'
    '\n\n'
    'Remember, this image is one element of a larger response. The task is'
    ' only to improve the image prompt, NOT write a prompt to answer the user'
    ' directly.\n'
    'Return ONLY the improved image generation prompt without explanations or metadata.'
)

refine_tikz_task_template = (
    'As an expert prompt engineer for TikZ diagrams, improve the following'
    ' TikZ prompt to produce better results. '
    'Your prompt will be used to generate a TikZ diagram for an individual'
    ' figure in a multimodal response to the user prompt shown below. '
    'You can think of this as a figure or diagram within a scientific paper.'
    '\n\n'
    'Original user query: {user_prompt}'
    '\n\n'
    'Current TikZ prompt to refine: {task_prompt}'
    '\n\n'
    'Improve the prompt by:\n'
    '1. Specifying the elements and structure of the diagram\n'
    '2. Clarifying the relationships between components\n'
    '3. Including any necessary labels, annotations, or captions\n'
    '4. Ensuring the diagram is clear, informative, and visually appealing\n'
    '5. Providing any additional context or instructions for the diagram'
    '\n\n'
    'Remember, this TikZ diagram is one element of a larger response. The task'
    ' is only to improve the TikZ prompt, NOT write a prompt to answer the user'
    ' directly.\n'
    'Return ONLY the enhanced TikZ generation prompt without additional text.'
)
