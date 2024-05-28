from flask import Flask, request, render_template
from solve_board import solve
from utils import validate_board, format_user_input

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_board():
    try:
        data = request.form
        board = format_user_input(data)
        if not validate_board(board):
            return render_template('index.html', error_message="Invalid board format")
        word_list = solve(board)
        return render_template('index.html', response=word_list)
    except Exception as e:
        error_message = str(e)
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)