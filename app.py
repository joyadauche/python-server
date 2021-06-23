from flask import Flask
from flask_restful import Api

from resources.home import Home
from resources.tone import Tone

app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(Tone, '/api/tone')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)