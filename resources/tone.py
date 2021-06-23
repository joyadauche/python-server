import random
from flask_restful import Resource

class Tone(Resource):
    def get(self):
        tone = ['humorous', 'ironic' , 'cynical']
        random_index = random.randint(0,len(tone)-1)

        return {'tone': tone[random_index]}, 200