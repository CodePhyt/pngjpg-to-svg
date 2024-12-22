from flask import Flask, render_template, request, send_file
import os
from werkzeug.utils import secure_filename
from converter import convert_to_svg
import tempfile
import shutil

app = Flask(__name__)

# Configure upload settings
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400
    
    if not allowed_file(file.filename):
        return 'Invalid file type. Please upload a PNG or JPG image.', 400

    temp_input = None
    temp_output = None
    try:
        # Create temporary directory
        temp_dir = tempfile.mkdtemp()
        
        # Save input file
        input_path = os.path.join(temp_dir, secure_filename(file.filename))
        file.save(input_path)
        
        # Create output path
        output_path = os.path.join(temp_dir, 'output.svg')
        
        # Convert the image
        convert_to_svg(input_path, output_path)

        # Read the SVG file
        with open(output_path, 'rb') as f:
            svg_content = f.read()

        return svg_content, 200, {
            'Content-Type': 'image/svg+xml',
            'Content-Disposition': f'attachment; filename={os.path.splitext(file.filename)[0]}.svg'
        }

    except Exception as e:
        return str(e), 500
        
    finally:
        # Clean up temporary directory and all its contents
        try:
            if temp_dir and os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
        except Exception:
            pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)
