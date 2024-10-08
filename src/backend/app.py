from flask import Flask, request, jsonify
from flask_cors import CORS
from wordle import Wordle

app = Flask(__name__)
CORS(app)
wordle = Wordle()
print(wordle.target_word)

@app.route('/handle-input', methods=['GET'])
def handle_input():
    word = request.args['word']
    
    legal = word in wordle.word_bank

    marking = []
    if legal:
        marking = wordle.guess_handler.mark_guess(word)
      
    return jsonify({'word': word, 'legal': legal, 'marking': marking}), 200



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)