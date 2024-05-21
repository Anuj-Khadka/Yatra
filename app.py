from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test-static')
def test_static():
    return f'<link rel="stylesheet" href="{url_for("static", filename="css/style.css")}"> Static file test.'


if __name__ == '__main__':
    app.run(debug=True)