from flask import Flask
from flasgger import LazyJSONEncoder
from flask_cors import CORS
import requests

app = Flask(__name__)


CORS(app)

@app.route("/")
def hello_world():
    return "<h1>Hello: World</h1>"


@app.route("/Stop/<id>")
def Stop(id):
    url = f'https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-circulation-passages-tr&q=&rows=100&sort=-idarret&facet=Point+d%27arr%C3%AAt&refine.Point+d%27arr%C3%AAt={id}'
    return sendRequest(url)


def sendRequest(url):
    return requests.get(url).json()


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5001)
