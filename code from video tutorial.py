from flask import Flask

app = Flask(__name__)
def home():
    return "<h1>Welcome<h1> This is the home page"

if __name__ == "__main__":
    app.run()