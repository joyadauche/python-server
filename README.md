# TONE API
## An API that randomly returns the tone of a user.

## Resources
### Tone
#### GET /api/tone - randomly return a tone

### Home
#### GET / - home page

## Run Server
- `git clone https://github.com/joyadauche/python-server.git`
- `cd python-server`
- To run with [Docker](https://docs.docker.com/get-docker/):
    - `docker build -t tone--flask-python-server .`     
    - `docker run -it -p 5000:5000 tone--flask-python-server`
- To run without docker:
    - `npm start`

## Run Tests
`python test.py`