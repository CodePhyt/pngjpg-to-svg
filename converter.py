import cv2
import numpy as np
from PIL import Image
import svgwrite
import os
import base64
from io import BytesIO

def image_to_data_url(img):
    """Convert PIL image to base64 data URL"""
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

def convert_to_svg(image_path, svg_path, params=None):
    """
    Convert image to SVG with exact pixel-perfect reproduction
    """
    # Open the image
    img = Image.open(image_path)
    
    # Convert RGBA to RGB if necessary
    if img.mode == 'RGBA':
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        img = background
    
    # Get image dimensions
    width, height = img.size
    
    # Create SVG drawing with exact dimensions
    dwg = svgwrite.Drawing(svg_path, size=(width, height))
    
    # Convert image to data URL
    img_data = image_to_data_url(img)
    
    # Add the image to SVG as a single element
    dwg.add(dwg.image(
        href=img_data,
        insert=(0, 0),
        size=(width, height)
    ))
    
    # Save the SVG file
    dwg.save()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert JPG/PNG images to SVG')
    parser.add_argument('input', help='Input image file')
    parser.add_argument('-o', '--output', help='Output SVG file')
    args = parser.parse_args()
    
    input_path = args.input
    output_path = args.output or os.path.splitext(input_path)[0] + '.svg'
    
    try:
        convert_to_svg(input_path, output_path)
        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {str(e)}")
