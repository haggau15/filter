from flask import Flask, request, jsonify
from flask_cors import CORS

# Create a Flask app
app = Flask(__name__)
CORS(app)


# Define a GET endpoint
@app.route('/filter', methods=['POST'])
def hello():
    request_body = request.json
    return jsonify(request_body)


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5001)
