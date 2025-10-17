import os
import secrets
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.errorhandler(413)
def file_too_large(e):
    return render_template('error.html', message="File too large! Max 2MB allowed."), 413

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
      return render_template('error.html', message="No file selected!")
    
    file = request.files['file']
    if file.filename == '':
        return render_template('error.html', message="No file selected!")

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        random_hex = secrets.token_hex(8)
        new_filename = random_hex + "_" + filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        file.save(filepath)
        return render_template('upload_success.html', filename=new_filename)
    else:
        return render_template('error.html', message="Invalid file type! Only .png, .jpg, .jpeg, .pdf allowed.")

if __name__ == '__main__':
    app.run(debug=True)
