import random
from flask_restful import Resource

class Home(Resource):
    def get(self):
        return {'Message': 'Welcome to the tone API - go to /api/tone'}, 200