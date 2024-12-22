# PNG/JPG to SVG Converter

A simple web application that converts PNG and JPG images to SVG format while maintaining exact pixel-perfect quality. The converter creates SVGs that are identical to the input images, making it perfect for when you need your images in SVG format without any loss of quality.

## Features

- Exact 1:1 conversion from PNG/JPG to SVG
- Perfect color preservation
- Handles transparency
- Simple web interface
- Direct file download
- Local processing (no data sent to external servers)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pngjpg-to-svg.git
cd pngjpg-to-svg
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the web server:
```bash
python app.py
```

2. Open your web browser and go to:
```
http://localhost:5000
```

3. Use the web interface to:
   - Select a PNG or JPG file
   - Click "Convert to SVG"
   - The converted SVG will automatically download

## How It Works

The converter works by:
1. Reading the input image
2. Creating an SVG container with the exact dimensions
3. Embedding the original image data in base64 format
4. Preserving all original pixels and colors perfectly

This approach ensures that the output SVG looks exactly like the input image, with no quality loss or alterations.

## Dependencies

- Flask
- Pillow (PIL)
- svgwrite
- numpy
- opencv-python

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
