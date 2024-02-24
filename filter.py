from flask import Flask, request, jsonify
from flask_cors import CORS

# Create a Flask app
app = Flask(__name__)
CORS(app)


@app.route('/filter', methods=['POST'])
def low_to_high():
    request_body = request.json
    temp = []
    for i in range(0, len(request_body)-1):
        # Score is initally set to a higher number than possible in the google score
        for n in range(0, len(request_body)-1):
            if request_body[n]['score'] > request_body[n + 1]['score']:
                request_body[n], request_body[n + 1] = request_body[n + 1], request_body[n]

    return jsonify(request_body)


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5001)
