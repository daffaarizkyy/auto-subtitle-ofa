import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

from subtitle import subtitle

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['MAX_CONTENT_LENGTH'] = 1000 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.mp4', '.mkv', '.3gp', '.avi']
app.config['UPLOAD_PATH'] = 'uploads'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload')
def upload_page():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        video = os.path.splitext(filename)[0]
        if file_ext.lower() not in app.config['UPLOAD_EXTENSIONS']:
            message = "Format File Not Allowed"
            return render_template('upload.html', message=message)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        subtitle(video, file_ext)
    return render_template('upload.html', filename=video)


@app.route('/download/<filename>')
def download_page(filename):
    path = f"{os.path.join(app.config['UPLOAD_PATH'], filename)}-subtitle.srt"
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run()
