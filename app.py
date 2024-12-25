from flask import Flask, request, render_template, jsonify, send_file
import os
from werkzeug.utils import secure_filename
from converter import convert_to_svg
import tempfile
import shutil

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    temp_dir = None
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file provided'})

        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'})

        if file:
            # Create a temporary directory for processing
            temp_dir = tempfile.mkdtemp()
            
            # Secure the filename
            filename = secure_filename(file.filename)
            
            # Save input file to temporary directory
            input_path = os.path.join(temp_dir, filename)
            file.save(input_path)
            
            # Generate output path
            output_filename = os.path.splitext(filename)[0] + '.svg'
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            
            # Convert the file
            convert_to_svg(input_path, output_path)
            
            # Return success response with file info
            return jsonify({
                'success': True,
                'output_filename': output_filename,
                'output_path': f'/download/{output_filename}'
            })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
    
    finally:
        # Clean up temporary directory
        if temp_dir and os.path.exists(temp_dir):
            try:
                shutil.rmtree(temp_dir)
            except Exception as e:
                print(f"Error cleaning up temporary directory: {str(e)}")

@app.route('/download/<filename>')
def download_file(filename):
    try:
        return send_file(
            os.path.join(app.config['UPLOAD_FOLDER'], filename),
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
