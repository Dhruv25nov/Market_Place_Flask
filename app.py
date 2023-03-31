from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/about/<name>")
def greet_user(name):
    return f"<h1>How are your {name}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
