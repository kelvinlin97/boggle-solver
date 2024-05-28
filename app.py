from flask import Flask, request, render_template
from solve_board import solve

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_board():
    data = request.get_json()
    board = data.get('board')
    solve(board)
    return "hi'"

if __name__ == '__main__':
    app.run(debug=True)