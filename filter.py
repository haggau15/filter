import json

from flask import Flask, request, jsonify
from flask_cors import CORS

# Create a Flask app
app = Flask(__name__)
CORS(app)


@app.route('/filter/high', methods=['POST'])
def high_to_low():
    request_body = request.json
    for i in range(0, len(request_body) - 1):
        # Score is initally set to a higher number than possible in the google score
        for n in range(0, len(request_body) - 1):
            if request_body[n]['score'] < request_body[n + 1]['score']:
                request_body[n], request_body[n + 1] = request_body[n + 1], request_body[n]

    return jsonify(request_body)


@app.route('/filter/low', methods=['POST'])
def low_to_high():
    request_body = request.json
    for i in range(0, len(request_body) - 1):
        # Score is initally set to a higher number than possible in the google score
        for n in range(0, len(request_body) - 1):
            if request_body[n]['score'] > request_body[n + 1]['score']:
                request_body[n], request_body[n + 1] = request_body[n + 1], request_body[n]

    return jsonify(request_body)


@app.route('/filter/comments/low', methods=['POST'])
def comments_low():
    request_body = request.json
    reviews = request_body[1]['reviews']
    words = get_words()
    for review in reviews:
        for word in json.loads(review)['text'].split():
            #print(" "+word+" ")
            if word in words:
                print("match")

    return jsonify(request_body)


def get_words():
    with open('bad_words', 'r') as file:
        # Read all lines from the file and store them in a list
        words = file.readlines()
        words = [string.rstrip('\n') for string in words]
    return [string.lstrip() for string in words]


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5001)
