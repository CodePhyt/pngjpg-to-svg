from PIL import Image, ImageDraw
import math

def create_pattern():
    # Create a new image with a white background
    width = 600
    height = 400
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Draw a pattern of circles
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD']
    radius = 30
    spacing = 70

    for y in range(0, height, spacing):
        offset = (y // spacing) % 2 * (spacing // 2)
        for x in range(-spacing // 2, width + spacing // 2, spacing):
            color = colors[((x + y) // spacing) % len(colors)]
            draw.ellipse([x + offset - radius, y - radius, 
                         x + offset + radius, y + radius], 
                         fill=color)

    # Add some connecting lines
    for y in range(0, height, spacing):
        offset = (y // spacing) % 2 * (spacing // 2)
        for x in range(-spacing // 2, width + spacing // 2, spacing):
            if x < width - spacing:
                # Draw horizontal lines
                draw.line([x + offset + radius, y, 
                          x + offset + spacing - radius, y], 
                          fill='#2C3E50', width=2)

    # Save the image
    image.save('examples/pattern.png')

if __name__ == "__main__":
    create_pattern()
