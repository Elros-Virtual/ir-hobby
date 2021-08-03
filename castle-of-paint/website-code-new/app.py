from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/canvaspainting')
def canvaspainting():
    return render_template('canvaspainting.html')


@app.route('/miniaturepainting')
def miniaturepainting():
    return render_template('miniaturepainting.html')


@app.route('/digitalart')
def digitalart():
    return render_template('digitalart.html')


@app.route('/pencilsketching')
def pencilsketching():
    return render_template('pencilsketching.html')


@app.route('/articles')
def articles():
    return render_template('articles.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)
