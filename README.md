# TONE API
An API that randomly returns the tone of a user.

## Postman Documentation
- [API Service Doc](https://documenter.getpostman.com/view/1407713/TzecB4jd)
- [API Service Test](https://www.getpostman.com/collections/81ee9e8511bb4c54ce25)

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
    - `python app.py`

## Run Tests
`python test.py`