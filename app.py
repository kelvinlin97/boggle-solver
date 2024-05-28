from flask import Flask, jsonify, request, render_template
from solve_board import solve
from utils import validate_board

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_board():
    data = request.get_json()
    board = data.get('board')
    validate_board(board)


    if not validate_board(board):
        return jsonify({"error": "Invalid board: Board must contain only lowercase letters"}), 400
    solve(board)
    return "hi'"

if __name__ == '__main__':
    app.run(debug=True)