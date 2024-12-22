from PIL import Image, ImageDraw
import math

# Create a new image with a white background
width = 500
height = 400
image = Image.new('RGB', (width, height), 'white')

# Create a drawing object
draw = ImageDraw.Draw(image)

# Draw some shapes with different colors
# Blue rectangle
draw.rectangle([50, 50, 200, 150], fill='blue')

# Red circle
draw.ellipse([250, 100, 350, 200], fill='red')

# Green triangle
draw.polygon([(400, 50), (450, 150), (350, 150)], fill='green')

# Purple star
star_points = [
    (150, 250), (170, 300), (220, 310),
    (180, 350), (190, 400), (150, 370),
    (110, 400), (120, 350), (80, 310),
    (130, 300)
]
draw.polygon(star_points, fill='purple')

# Orange hexagon
center = (350, 300)
radius = 50
points = []
for i in range(6):
    angle = i * math.pi / 3
    x = center[0] + radius * math.cos(angle)
    y = center[1] + radius * math.sin(angle)
    points.append((x, y))
draw.polygon(points, fill='orange')

# Save the image
image.save('test.png')
