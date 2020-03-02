from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
import os

# const vars
LAMBDA__BASE_URL = 'https://lambda-treasure-hunt.herokuapp.com'

# load_dotenv()
# KYLES_KEY = os.getenv("KYLE_KEY")
# print(KYLES_KEY)

# load up env vars
load_dotenv()
app = Flask(__name__)

# hit the productoin server with a header of the following: Authorization: Token USER_TOKEN_HERE
@app.route('/init', methods=["GET"])
def init_player():
    # grab the user token from the HTTP request obj
    token = request.headers["Authorization"]
    # setup req headers
    headers = {
        "Authorization": f'Token {token}'
    }

    # send a request to Lambda
    r = requests.get(f'{LAMBDA__BASE_URL}/api/adv/init', headers=headers)
    return r.json()


if __name__ == "__main__":
    app.run()
