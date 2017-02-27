from flask import Flask, render_template, request, url_for
import star

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        pattern = request.form['pattern']
        word = request.form['word']
        A = star.AsteriskPattern(pattern)
        result = str(A.check(word))
    else:
        pattern = "A*"
        word = "Adda"
        result = "True"
    return render_template('index.html', pattern=pattern, word=word, result=result)


if __name__ == '__main__':
    app.run()
