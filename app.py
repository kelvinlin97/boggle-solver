from flask import Flask, jsonify, request, render_template
from solve_board import solve
from utils import validate_board, format_user_input

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_board():
    data = request.form
    board = format_user_input(data)
    
    if not board or not validate_board(board):
        return jsonify({"error": "Invalid board: Board must be provided and contain only lowercase letters"}), 400
    
    word_list = solve(board)
    return jsonify({"words": word_list, "word_count": len(word_list)})

if __name__ == '__main__':
    app.run(debug=True)