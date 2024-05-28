from data.utils import validate_word

# TODO: validate board

placeholder = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]

def solve(board):
    # dfs board
        # explore path 
            # only visit node if node has not been visited already in current run (do not want to repeat)
            # once valid path (3 or more)
                # check if word has been seen already (found in another dfs call)
                    # if not seen, check if word is valid (from set of valid words)
                        # if valid, add word to seen
    
    valid_words = set()

    def dfs(x, y, marked, prev):  
        marked.add((x, y))
        cur = prev + board[x][y]    
        if len(cur) >= 3 and validate_word(cur):
            valid_words.add(cur)
        for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x - 1, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1)):
            if 0 <= dx < len(board) and 0 <= dy < len(board) and (dx, dy) not in marked:
                dfs(dx, dy, marked.copy(), cur)
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            dfs(i, j, set(), '')
    
    return list(valid_words)
    

res = solve(placeholder)
print(res)