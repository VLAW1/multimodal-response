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
    # 'Context:\n'
    # '- This text {before_context}.\n'
    # '- This text {after_context}.'
    # '\n\n'
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
    # 'Context:\n'
    # '- This image {before_context}.\n'
    # '- This image {after_context}.'
    # '\n\n'
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
