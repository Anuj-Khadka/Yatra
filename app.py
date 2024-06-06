from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test-static')
def test_static():
    return f'<link rel="stylesheet" href="{url_for("static", filename="css/style.css")}"> Static file test.'

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

