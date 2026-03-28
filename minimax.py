#!/usr/bin/env python3
"""minimax - Minimax with alpha-beta pruning (Tic-Tac-Toe demo)."""
import sys
def check_winner(board):
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in lines:
        if board[a]==board[b]==board[c]!=" ": return board[a]
    return None
def minimax(board, is_max, alpha=float('-inf'), beta=float('inf')):
    w = check_winner(board)
    if w == "X": return 1
    if w == "O": return -1
    if " " not in board: return 0
    if is_max:
        best = float('-inf')
        for i in range(9):
            if board[i]==" ":
                board[i]="X"; val=minimax(board, False, alpha, beta); board[i]=" "
                best=max(best, val); alpha=max(alpha, val)
                if beta<=alpha: break
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i]==" ":
                board[i]="O"; val=minimax(board, True, alpha, beta); board[i]=" "
                best=min(best, val); beta=min(beta, val)
                if beta<=alpha: break
        return best
def best_move(board, player="X"):
    is_max = player=="X"; best_val=float('-inf') if is_max else float('inf'); move=-1
    for i in range(9):
        if board[i]==" ":
            board[i]=player; val=minimax(board, not is_max); board[i]=" "
            if (is_max and val>best_val) or (not is_max and val<best_val):
                best_val=val; move=i
    return move, best_val
def display(board):
    for i in range(0,9,3): print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
    print()
if __name__=="__main__":
    board = list("         ")
    if len(sys.argv) > 1: board = list(sys.argv[1].replace(".",  " ").ljust(9)[:9])
    display(board); move, val = best_move(board)
    print(f"Best move: position {move} (value: {val})")
