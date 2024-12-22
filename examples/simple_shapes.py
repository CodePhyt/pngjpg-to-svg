from PIL import Image, ImageDraw

# Create a new image with a white background
width = 400
height = 300
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw basic shapes
# Rectangle
draw.rectangle([50, 50, 150, 100], fill='blue')

# Circle
draw.ellipse([200, 50, 300, 150], fill='red')

# Triangle
draw.polygon([(50, 200), (150, 200), (100, 150)], fill='green')

# Save the image
image.save('examples/simple_shapes.png')
