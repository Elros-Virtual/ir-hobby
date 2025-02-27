from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/elements')
def elements():
    return render_template('elements.html')


@app.route('/generic')
def generic():
    return render_template('generic.html')


@app.route('/canvaspainting')
def canvaspainting():
    return render_template('canvaspainting.html')


@app.route('/miniturepainting')
def miniturepainting():
    return render_template('miniturepainting.html')


@app.route('/digitalart')
def digitalart():
    return render_template('digitalart.html')


@app.route('/pencilsketching')
def pencilsketching():
    return render_template('pencilsketching.html')


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)
