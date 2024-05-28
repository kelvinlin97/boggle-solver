from utils import load_data
import time

placeholder = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]

def solve(board):
    # dfs board
        # explore path 
            # only visit node if node has not been visited already in current run (do not want to repeat)
            # once valid path (3 or more)
                # check if word has been seen already (found in another dfs call)
                    # if not seen, check if word is valid (from set of valid words)
                        # if valid, add word to seen
        # reduce calls by storing prefixes for frequently used words
    
    prefixes = load_data('prefixes.json')
    valid_words = load_data('valid_words.json')
    start_time = time.time()
    res = set()

    def dfs(x, y, prev):  
        char = board[x][y]
        cur = prev + char
        if cur not in prefixes:
            return
        if len(cur) >= 3 and cur in valid_words:
            res.add(cur)
        board[x][y] = '#'
        for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x - 1, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1)):
            if 0 <= dx < len(board) and 0 <= dy < len(board) and board[dx][dy] != '#':
                dfs(dx, dy, cur)
        board[x][y] = char
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            dfs(i, j, '')
    
    print("Found %d valid words in %f seconds" % (len(res), time.time() - start_time))
    return list(res)
    

res = solve(placeholder)