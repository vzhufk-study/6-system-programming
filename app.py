import os
from os.path import join, realpath

from flask import Flask, render_template, request, url_for
from os.path import dirname

from flask import send_from_directory
from werkzeug.utils import secure_filename, redirect

import star

app = Flask(__name__)
# Set default static file storage
app.config['UPLOAD_FOLDER'] = join(dirname(realpath(__file__)), 'static')


@app.route('/')
def index():
    # Home page
    return render_template('index.html')


asterisk = star.AsteriskPattern("*")
file = None


@app.route('/single', methods=['POST', 'GET'])
def single():
    if request.method == 'POST':
        pattern = request.form['pattern']
        word = request.form['word']
        # Call global var
        global asterisk
        asterisk = star.AsteriskPattern(pattern)
        result = str(asterisk.check(word))
    else:
        pattern = "A*"
        word = "Adda"
        result = "True"
    return render_template('single.html', pattern=pattern, word=word, result=result)


@app.route('/upload')
def upload():
    return render_template('file.html')


@app.route('/downloader', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        global file
        return file
    else:
        return redirect(url_for('upload'))


# TODO Front and split it to one lab.

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        global asterisk
        asterisk.file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        pattern = asterisk.pattern
        text = asterisk.text
        if len(asterisk.result) > 1:
            result = asterisk.result[0]
            result_sort = asterisk.result[1]
        else:
            result = ""
            result_sort = ""

        global file
        file = send_from_directory(directory=app.config['UPLOAD_FOLDER'], filename=filename, as_attachment=True)

        return render_template('file.html', pattern=pattern, text=text, result=result, result_sort=result_sort)


if __name__ == '__main__':
    app.run()
