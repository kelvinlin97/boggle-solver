from flask import Flask, request, render_template
from solve_board import solve
from utils import validate_board

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_board():
<<<<<<< Updated upstream
    data = request.get_json()
    board = data.get('board')
    validate_board(board)


    if not validate_board(board):
        return jsonify({"error": "Invalid board: Board must contain only lowercase letters"}), 400
    solve(board)
    return "hi'"
=======
    try:
        data = request.form
        board = format_user_input(data)
        validate_board(board)
        word_list = solve(board)
        return render_template('index.html', response=word_list)
    except Exception as e:
        error_message = str(e)
        return render_template('index.html', error_message=error_message)
>>>>>>> Stashed changes

if __name__ == '__main__':
    app.run(debug=True)