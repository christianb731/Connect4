from flask import Flask, request, jsonify
from flask_restful import Api
from gameService import CalculateWinner
app = Flask(__name__)
api = Api(app)

@app.route('/game/connect4')
def play():
    moves = request.args.get("moves")
    moves = list(moves)
    return jsonify(CalculateWinner(moves))

if __name__ == "__main__":
   app.run(debug=True, port=9615)