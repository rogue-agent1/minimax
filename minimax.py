#!/usr/bin/env python3
"""minimax — Minimax with alpha-beta pruning for game trees. Zero deps."""

def minimax(node, depth, maximizing, evaluate, children, alpha=float('-inf'), beta=float('inf')):
    kids = children(node)
    if depth == 0 or not kids:
        return evaluate(node), None
    best_move = None
    if maximizing:
        value = float('-inf')
        for child in kids:
            v, _ = minimax(child, depth-1, False, evaluate, children, alpha, beta)
            if v > value:
                value, best_move = v, child
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, best_move
    else:
        value = float('inf')
        for child in kids:
            v, _ = minimax(child, depth-1, True, evaluate, children, alpha, beta)
            if v < value:
                value, best_move = v, child
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value, best_move

# Tic-tac-toe demo
def ttt_winner(board):
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in lines:
        if board[a] == board[b] == board[c] and board[a] != '.':
            return board[a]
    return None

def ttt_evaluate(state):
    board, player = state
    w = ttt_winner(board)
    if w == 'X': return 10
    if w == 'O': return -10
    return 0

def ttt_children(state):
    board, player = state
    if ttt_winner(board): return []
    kids = []
    opp = 'O' if player == 'X' else 'X'
    for i in range(9):
        if board[i] == '.':
            nb = list(board); nb[i] = player
            kids.append((tuple(nb), opp))
    return kids

def show_board(board):
    for r in range(3):
        print("  " + " ".join(board[r*3:r*3+3]))

def main():
    board = tuple(".........")
    player = 'X'
    print("Minimax plays perfect tic-tac-toe (X=max, O=min):\n")
    state = (board, player)
    while True:
        w = ttt_winner(state[0])
        if w: print(f"\n  Winner: {w}!"); break
        if '.' not in state[0]: print("\n  Draw!"); break
        show_board(state[0])
        val, best = minimax(state, 9, state[1]=='X', ttt_evaluate, ttt_children)
        move = next(i for i in range(9) if state[0][i] != best[0][i])
        print(f"  {state[1]} plays position {move} (eval={val})\n")
        state = best

if __name__ == "__main__":
    main()
