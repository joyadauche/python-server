from flask.typing import StatusCode
from werkzeug.wrappers import response
from app import app
import unittest
import json

class Test(unittest.TestCase):
    
    def test_tone_response_code(self):
        tester = app.test_client(self)
        response = tester.get("/api/tone")
        status_code = response.status_code

        self.assertEqual(status_code, 200)
    
    def test_tone_response_content(self):
        tester = app.test_client(self)
        response = tester.get("/api/tone")
        data = json.loads(response.get_data(as_text=True))
        self.assertIn(data['tone'], ['humorous', 'ironic' , 'cynical'])


if __name__ == '__main__':
    unittest.main()