from wsgi import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"