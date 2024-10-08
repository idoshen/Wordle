from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/handle-input', methods=['GET'])
def handle_input():
    word = request.args['word']
    hi(word)
    return jsonify({'message': word}), 200

def hi(word):
    print(word)

if __name__ == '__main__':

    app.run(debug=True)