from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_board():
    data = request.get_json()
    board = data.get('board')
    return "hi'"

def solve_boggle(board):
    return "hi"

if __name__ == '__main__':
    app.run(debug=True)