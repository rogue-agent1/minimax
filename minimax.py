#!/usr/bin/env python3
"""Minimax - Game tree search with alpha-beta pruning for two-player games."""
import sys, math

class TicTacToe:
    def __init__(self): self.board = [" "]*9
    def moves(self): return [i for i in range(9) if self.board[i] == " "]
    def make(self, pos, player): b = self.board[:]; b[pos] = player; t = TicTacToe(); t.board = b; return t
    def winner(self):
        lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b,c in lines:
            if self.board[a] == self.board[b] == self.board[c] != " ": return self.board[a]
        return None
    def is_terminal(self): return self.winner() is not None or not self.moves()
    def display(self):
        for i in range(3):
            print("  " + " | ".join(self.board[i*3:(i+1)*3]))
            if i < 2: print("  ---------")

def minimax(state, depth, alpha, beta, maximizing, nodes=[0]):
    nodes[0] += 1
    w = state.winner()
    if w == "X": return 10 - depth
    if w == "O": return depth - 10
    if not state.moves(): return 0
    if maximizing:
        val = -math.inf
        for m in state.moves():
            val = max(val, minimax(state.make(m, "X"), depth+1, alpha, beta, False, nodes))
            alpha = max(alpha, val)
            if beta <= alpha: break
        return val
    else:
        val = math.inf
        for m in state.moves():
            val = min(val, minimax(state.make(m, "O"), depth+1, alpha, beta, True, nodes))
            beta = min(beta, val)
            if beta <= alpha: break
        return val

def best_move(state, player="X"):
    best = None; best_val = -math.inf if player == "X" else math.inf
    nodes = [0]
    for m in state.moves():
        val = minimax(state.make(m, player), 0, -math.inf, math.inf, player == "O", nodes)
        if (player == "X" and val > best_val) or (player == "O" and val < best_val):
            best_val = val; best = m
    return best, best_val, nodes[0]

def main():
    game = TicTacToe()
    print("=== Minimax with Alpha-Beta ===\n")
    move, val, nodes = best_move(game, "X")
    print(f"Best first move for X: position {move} (value={val}, {nodes} nodes searched)")
    game = game.make(0, "X").make(4, "O").make(8, "X")
    print("\nMid-game:"); game.display()
    move, val, nodes = best_move(game, "O")
    print(f"\nBest move for O: position {move} (value={val}, {nodes} nodes)")

if __name__ == "__main__":
    main()
