#!/usr/bin/env python3
"""minimax: Minimax with alpha-beta pruning for two-player games."""
import sys

def minimax(state, depth, maximizing, evaluate, get_moves, apply_move, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or not get_moves(state):
        return evaluate(state), None
    best_move = None
    if maximizing:
        value = float('-inf')
        for move in get_moves(state):
            new_state = apply_move(state, move)
            score, _ = minimax(new_state, depth-1, False, evaluate, get_moves, apply_move, alpha, beta)
            if score > value:
                value, best_move = score, move
            alpha = max(alpha, value)
            if beta <= alpha: break
        return value, best_move
    else:
        value = float('inf')
        for move in get_moves(state):
            new_state = apply_move(state, move)
            score, _ = minimax(new_state, depth-1, True, evaluate, get_moves, apply_move, alpha, beta)
            if score < value:
                value, best_move = score, move
            beta = min(beta, value)
            if beta <= alpha: break
        return value, best_move

def test():
    # Simple number picking game: pick from list, max wants high sum, min wants low
    def evaluate(state):
        return state["score"]
    def get_moves(state):
        return list(range(len(state["nums"]))) if state["nums"] else []
    def apply_move(state, move):
        nums = list(state["nums"])
        val = nums.pop(move)
        mult = 1 if state["turn"] == "max" else -1
        return {"nums": nums, "score": state["score"] + mult * val,
                "turn": "min" if state["turn"] == "max" else "max"}
    state = {"nums": [3, 1, 5, 2], "score": 0, "turn": "max"}
    score, move = minimax(state, 4, True, evaluate, get_moves, apply_move)
    assert move is not None
    # Tic-tac-toe position: X can win
    board = list("X.O" "..X" "O..")
    def ttt_eval(b):
        lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,c,d in lines:
            if b[a]==b[c]==b[d]=="X": return 10
            if b[a]==b[c]==b[d]=="O": return -10
        return 0
    def ttt_moves(b):
        if abs(ttt_eval(b)) == 10: return []
        return [i for i in range(9) if b[i] == "."]
    def ttt_apply(b, move):
        new = list(b)
        empty = sum(1 for c in b if c == ".")
        new[move] = "X" if empty % 2 == 1 else "O"
        return new
    score2, move2 = minimax(board, 9, True, ttt_eval, ttt_moves, ttt_apply)
    assert score2 >= 0  # X should at least draw or win
    print("All tests passed!")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print("Usage: minimax.py test")
