import json

from flask import Flask, request, jsonify
from flask_cors import CORS

# Create a Flask app
app = Flask(__name__)
CORS(app)


# toBeDone
@app.route('/comment/low', methods=['POST'])
def comment_low():
    request_body = request.json

    return jsonify(request_body)

@app.route('/filter/high', methods=['POST'])
def high_to_low():
    request_body = request.json
    # Implementation of bubblesort using the user score given to a location
    for i in range(0, len(request_body) - 1):
        for n in range(0, len(request_body) - 1):
            if request_body[n]['score'] < request_body[n + 1]['score']:
                request_body[n], request_body[n + 1] = request_body[n + 1], request_body[n]

    return jsonify(request_body)


@app.route('/filter/low', methods=['POST'])
def low_to_high():
    request_body = request.json
    # Implementation of bubblesort using the user score given to a location
    for i in range(0, len(request_body) - 1):
        for n in range(0, len(request_body) - 1):
            if request_body[n]['score'] > request_body[n + 1]['score']:
                request_body[n], request_body[n + 1] = request_body[n + 1], request_body[n]

    return jsonify(request_body)


# Sorts resturants by their reviews from worst to best
@app.route('/filter/comments/low', methods=['POST'])
def comments_low():
    request_body = request.json
    request_body = get_comment_score(request_body)
    for i in range(0, len(request_body) - 1):
        for n in range(0, len(request_body) - 1):
            if request_body[n]['comment_score'] < request_body[n + 1]['comment_score']:
                request_body[n], request_body[n + 1] = request_body[n + 1], request_body[n]

    return jsonify(request_body)


# Sorts resturants by their reviews from best to worst
@app.route('/filter/comments/high', methods=['POST'])
def comments_high():
    request_body = request.json
    request_body = get_comment_score(request_body)
    for i in range(0, len(request_body) - 1):
        for n in range(0, len(request_body) - 1):
            if request_body[n]['comment_score'] > request_body[n + 1]['comment_score']:
                request_body[n], request_body[n + 1] = request_body[n + 1], request_body[n]

    return jsonify(request_body)


def get_comment_score(request_body):
    words = get_words()
    counter = 0
    # Loops through every word in every review of a location and checks if it is in the bad_words file
    # Adds the score from how negative the comments are as a variable in the jsonobject
    for place in request_body:  # Contains every resturant for one area
        for review in place['reviews']:  # Contains 5 reviews for every resturant
            for word in json.loads(review)[
                'text'].split():  # Checks every word of each review to a list of negative words
                if word.lower() in words:
                    counter += 1
        place['comment_score'] = counter
        counter = 0
    return request_body


def get_words():
    with open('bad_words', 'r') as file:
        # Read all lines from the file and store them in a list
        words = file.readlines()
        words = [string.lower() for string in words]  # Sets all string to lowercase
        words = [string.rstrip('\n') for string in words]  # Removes new line character for every word
    return [string.lstrip() for string in words]  # All whitespace before the word is removed


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5001)
