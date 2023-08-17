from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/qwe/')
def hello():
    return 'Hello, World!'

# with command below is possible to use "py hello.py"
# if __name__ == "__main__":
    # app.run()
