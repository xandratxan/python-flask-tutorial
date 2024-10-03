"""test Flask with this"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

# Run app at command prompt:
# > cd flask-intro/
# > flask --app hello run