import os
import subprocess
import uuid
import platform
from pathlib import Path


def compile_tikz(tikz_code: str, output_dir: str = 'tikz_images') -> str:
    """
    Compile TikZ code into a PDF then convert to PNG.

    Parameters
    ----------
    tikz_code : str
        The TikZ code to compile
    output_dir : str
        Directory to save the output image

    Returns
    -------
    str
        Path to the generated PNG image
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create a unique ID for this compilation
    unique_id = str(uuid.uuid4())[:8]

    # Create paths
    tex_path = Path(output_dir) / f'{unique_id}.tex'
    pdf_path = Path(output_dir) / f'{unique_id}.pdf'
    png_path = Path(output_dir) / f'{unique_id}.png'

    # Create a minimal LaTeX document with the TikZ code
    tex_content = (
        '\\documentclass[border=10pt]{{standalone}}\n'
        '\\usepackage{{tikz}}\n'
        '\\usepackage{{pgfplots}}\n'
        '\\pgfplotsset{{compat=1.18}}\n'
        '\\usetikzlibrary{{arrows,shapes,positioning,fit,calc,'
        'decorations.pathreplacing,decorations.markings}}\n'
        '\n'
        '\\begin{{document}}\n'
        '{tikz_code}\n'
        '\\end{{document}}\n'
    )

    # Write the LaTeX file
    with open(tex_path, 'w') as f:
        f.write(tex_content.format(tikz_code=tikz_code))

    try:
        # Find the pdflatex executable
        if platform.system() == 'Darwin':  # macOS
            pdflatex_cmd = '/Library/TeX/texbin/pdflatex'
        else:
            pdflatex_cmd = 'pdflatex'

        # Compile with pdflatex
        subprocess.run(
            [
                pdflatex_cmd,
                '-interaction=nonstopmode',
                '-output-directory',
                output_dir,
                tex_path,
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        # Convert PDF to PNG using convert (from ImageMagick)
        subprocess.run(
            [
                'convert',
                '-density',
                '300',
                pdf_path,
                '-quality',
                '90',
                png_path,
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        # Return the path to the PNG
        return str(png_path)

    except subprocess.CalledProcessError:
        # If compilation fails, return None
        return None
