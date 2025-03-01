import re
import os
import requests
from urllib.parse import urlparse

from src.models.response import MultimodalResponse


def extract_code_blocks(text: str) -> str:
    """Format code blocks in markdown properly."""
    pattern = r'```(.*?)```'

    def replace_block(match):
        block = match.group(1)
        if '\n' in block:
            lang, *lines = block.split('\n', 1)
            return f'```{lang}\n{lines[0]}```'
        return f'```{block}```'

    return re.sub(pattern, replace_block, text, flags=re.DOTALL)


def download_image(url: str, save_path: str) -> bool:
    """
    Download an image from a URL and save it locally.

    Parameters
    ----------
    url : str
        The image URL
    save_path : str
        Path to save the downloaded image

    Returns
    -------
    bool
        True if download succeeded, False otherwise
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except Exception:
        # If download fails for any reason, return False
        return False


def save_response_to_html(
    response: MultimodalResponse, filepath: str, title: str | None = None
) -> None:
    """
    Save a multimodal response as an HTML file.

    Parameters
    ----------
        response : MultimodalResponse
            The MultimodalResponse to save
        filepath : str
            Path where the HTML file should be saved
        title : str
            Optional title for the HTML page. None by default.
    """
    # Create images directory next to the HTML file
    html_dir = os.path.dirname(os.path.abspath(filepath))
    images_dir = os.path.join(html_dir, 'images')
    os.makedirs(images_dir, exist_ok=True)

    html = ['<!DOCTYPE html>', '<html>', '<head>']
    html.append("<meta charset='utf-8'>")
    html.append(
        "<meta name='viewport' content='width=device-width, initial-scale=1'>"
    )
    html.append(f'<title>{title or "Multimodal Response"}</title>')
    html.append('<style>')
    html.append(
        'body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }'
    )
    html.append('img { max-width: 100%; height: auto; }')
    html.append(
        '.caption { font-style: italic; color: #666; margin-top: 5px; }'
    )
    html.append('</style>')
    html.append('</head>')
    html.append('<body>')

    if title:
        html.append(f'<h1>{title}</h1>')

    for i, element in enumerate(response.elements):
        if element.type == 'text':
            # Simple Markdown-like conversion for paragraphs
            paragraphs = element.content.split('\n\n')
            for p in paragraphs:
                if p.strip():
                    html.append(f'<p>{p}</p>')
        elif element.type == 'image':
            alt = element.alt_text or 'Generated image'

            # Extract filename from URL or create a unique one
            url_path = urlparse(element.url).path
            filename = os.path.basename(url_path)
            if not filename or '.' not in filename:
                # Create a filename with index and default extension
                filename = f'image_{i}.jpg'

            # Full path for saving the image
            image_path = os.path.join(images_dir, filename)
            # Relative path for HTML reference
            image_rel_path = f'images/{filename}'

            # Download the image and use local path if successful
            img_src = element.url
            if download_image(element.url, image_path):
                img_src = image_rel_path

            html.append('<figure>')
            html.append(f"<img src='{img_src}' alt='{alt}'>")
            if element.caption:
                html.append(
                    f"<figcaption class='caption'>{element.caption}</figcaption>"
                )
            html.append('</figure>')

    html.append('</body>')
    html.append('</html>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html))


def save_response_to_markdown(
    response: MultimodalResponse, filepath: str, title: str | None = None
) -> None:
    """
    Save a multimodal response as a Markdown file.

    Parameters
    ----------
        response : MultimodalResponse
            The MultimodalResponse to save
        filepath : str
            Path where the Markdown file should be saved
        title : str
            Optional title for the Markdown document. None by default.
    """
    # Create images directory next to the Markdown file
    md_dir = os.path.dirname(os.path.abspath(filepath))
    images_dir = os.path.join(md_dir, 'images')
    os.makedirs(images_dir, exist_ok=True)

    markdown = []

    # Add title if provided
    if title:
        markdown.append(f'# {title}\n')

    for i, element in enumerate(response.elements):
        if element.type == 'text':
            # Add text content directly
            markdown.append(f'{element.content}\n')
        elif element.type == 'image':
            # Extract filename from URL or create a unique one
            url_path = urlparse(element.url).path
            filename = os.path.basename(url_path)
            if not filename or '.' not in filename:
                # Create a filename with index and default extension
                filename = f'image_{i}.jpg'

            # Full path for saving the image
            image_path = os.path.join(images_dir, filename)
            # Relative path for Markdown reference
            image_rel_path = f'images/{filename}'

            # Download the image and use local path if successful
            img_src = element.url
            if download_image(element.url, image_path):
                img_src = image_rel_path

            # Add image in markdown format
            alt = element.alt_text or 'Generated image'
            image_md = f'![{alt}]({img_src})'

            # Add caption if provided
            if element.caption:
                image_md += f'\n\n_{element.caption}_'

            markdown.append(f'{image_md}\n')

    # Write markdown content to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown))
