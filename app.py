from flask import Flask
from flask import Response
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World! I'm using Flask."
    
@app.route("/message")
def message():
    return Response("Hello World! I'm using Flask.", mimetype='text/plain')