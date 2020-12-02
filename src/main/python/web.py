from flask import Flask, render_template, request, redirect, flash, url_for
import main
import urllib.request
from werkzeug.utils import secure_filename
from main import getPrediction
import os


app = Flask(__name__)
UPLOAD_FOLDER = 'src/main/python/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"

@app.route('/')
def index():
    return render_template('landing.html')
@app.route('/single')
def singleserve():
    return render_template('index.html')
@app.route('/multiple')
def multiserve():
    return render_template('multindex.html')

@app.route('/single', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER,filename))
            label= getPrediction(filename)
            return render_template("predicted.html", label = label)

@app.route('/multiple', methods=['POST'])
def submit_file_multi():
    labels = []
    if request.method == 'POST':
        files = request.files.getlist('multifile')
        print(files)
        for file in files:
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER,filename))
                label= getPrediction(filename)
                labels.append(label)
        return render_template("predictedmulti.html", labels = labels)

@app.route('/covid')
def serve_covid():
    return render_template('covid.html')
@app.route('/pneumonia')
def serve_pneu():
    return render_template('pneumonia.html')
@app.route('/tuberculosis')
def serve_tuber():
    return render_template('tuberculosis.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
