#!/usr/bin/env python3
"""minimax - Minimax with alpha-beta pruning for game trees."""
import sys

def minimax(state, depth, maximizing, evaluate, get_moves, apply_move, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or not get_moves(state):
        return evaluate(state), None
    best_move = None
    if maximizing:
        best = float('-inf')
        for move in get_moves(state):
            new_state = apply_move(state, move)
            val, _ = minimax(new_state, depth-1, False, evaluate, get_moves, apply_move, alpha, beta)
            if val > best:
                best = val
                best_move = move
            alpha = max(alpha, val)
            if beta <= alpha:
                break
    else:
        best = float('inf')
        for move in get_moves(state):
            new_state = apply_move(state, move)
            val, _ = minimax(new_state, depth-1, True, evaluate, get_moves, apply_move, alpha, beta)
            if val < best:
                best = val
                best_move = move
            beta = min(beta, val)
            if beta <= alpha:
                break
    return best, best_move

class TicTacToe:
    def __init__(self, board=None, turn="X"):
        self.board = board or [" "]*9
        self.turn = turn

    def winner(self):
        lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b,c in lines:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        return None

    def moves(self):
        if self.winner():
            return []
        return [i for i in range(9) if self.board[i] == " "]

    def apply(self, move):
        new_board = list(self.board)
        new_board[move] = self.turn
        return TicTacToe(new_board, "O" if self.turn == "X" else "X")

    def evaluate(self):
        w = self.winner()
        if w == "X": return 10
        if w == "O": return -10
        return 0

def test():
    game = TicTacToe()
    val, move = minimax(game, 9, True,
                        lambda s: s.evaluate(),
                        lambda s: s.moves(),
                        lambda s, m: s.apply(m))
    assert move is not None
    assert 0 <= move <= 8
    almost_won = TicTacToe(["X","X"," ","O","O"," "," "," "," "], "X")
    val, move = minimax(almost_won, 9, True,
                        lambda s: s.evaluate(),
                        lambda s: s.moves(),
                        lambda s, m: s.apply(m))
    assert move == 2
    assert val == 10
    block = TicTacToe(["X","X"," ","O"," "," "," "," "," "], "O")
    val, move = minimax(block, 9, False,
                        lambda s: s.evaluate(),
                        lambda s: s.moves(),
                        lambda s, m: s.apply(m))
    assert move == 2
    print("All tests passed!")

if __name__ == "__main__":
    test() if "--test" in sys.argv else print("minimax: Minimax with alpha-beta. Use --test")
