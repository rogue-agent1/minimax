import argparse

def tic_tac_toe():
    board = [" "] * 9
    def winner(b):
        lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,bb,c in lines:
            if b[a] == b[bb] == b[c] != " ": return b[a]
        return None
    def minimax(b, is_max, alpha, beta):
        w = winner(b)
        if w == "X": return -1
        if w == "O": return 1
        if " " not in b: return 0
        if is_max:
            best = -2
            for i in range(9):
                if b[i] == " ":
                    b[i] = "O"
                    best = max(best, minimax(b, False, alpha, beta))
                    b[i] = " "
                    alpha = max(alpha, best)
                    if beta <= alpha: break
            return best
        else:
            best = 2
            for i in range(9):
                if b[i] == " ":
                    b[i] = "X"
                    best = min(best, minimax(b, True, alpha, beta))
                    b[i] = " "
                    beta = min(beta, best)
                    if beta <= alpha: break
            return best
    def best_move(b):
        best_score, best_pos = -2, -1
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, False, -2, 2)
                b[i] = " "
                if score > best_score: best_score, best_pos = score, i
        return best_pos
    def show(b):
        for i in range(0, 9, 3):
            print(f" {b[i]} | {b[i+1]} | {b[i+2]}")
            if i < 6: print("---+---+---")
    print("Tic-Tac-Toe: You=X, AI=O")
    while True:
        show(board)
        w = winner(board)
        if w: print(f"{w} wins!"); break
        if " " not in board: print("Draw!"); break
        try:
            pos = int(input("Your move (0-8): "))
            if board[pos] != " ": print("Taken!"); continue
        except (ValueError, IndexError, EOFError): break
        board[pos] = "X"
        if " " in board and not winner(board):
            board[best_move(board)] = "O"

def main():
    p = argparse.ArgumentParser(description="Minimax game engine")
    p.add_argument("--ttt", action="store_true", help="Play Tic-Tac-Toe vs AI")
    p.add_argument("--bench", action="store_true", help="Benchmark minimax")
    args = p.parse_args()
    if args.ttt: tic_tac_toe()
    elif args.bench:
        board = [" "] * 9
        import time; t = time.time()
        # Count all nodes
        count = [0]
        def mm(b, is_max, a, be):
            count[0] += 1
            lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
            for x,y,z in lines:
                if b[x]==b[y]==b[z]!=" ": return -1 if b[x]=="X" else 1
            if " " not in b: return 0
            best = -2 if is_max else 2
            for i in range(9):
                if b[i]==" ":
                    b[i] = "O" if is_max else "X"
                    s = mm(b, not is_max, a, be)
                    b[i] = " "
                    if is_max: best=max(best,s); a=max(a,s)
                    else: best=min(best,s); be=min(be,s)
                    if be <= a: break
            return best
        mm(board, True, -2, 2)
        print(f"Nodes explored: {count[0]} in {time.time()-t:.3f}s")
    else: p.print_help()

if __name__ == "__main__":
    main()
