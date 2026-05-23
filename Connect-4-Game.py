# ================================================================
#  CONNECT-4 Game •  AI Edition
# ================================================================

import tkinter as tk
import math
import copy

class Connect_4_Game:
    def __init__(self):
        pass

    def create_board(self):
        board = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
            ]
        return board

    def print_board(self, board):
        print("\n")
        for row in board:
            print(row)
        print("\n")
           
    def Is_move_valid(self, board, col):
        if col < 0 or col > 6:
            return False
        return board[0][col] == 0

    def get_empty_row(self, board, col):
        for r in range(5, -1, -1):
            if board[r][col] == 0:
                return r
        return None
            
    def Do_move(self, board, col, piece):
        if not self.Is_move_valid(board, col):
            return False
        row = self.get_empty_row(board, col)
        if row is not None:
            board[row][col] = piece
            return True
        return False

    def winning_move(self, board, piece):
        # Horizontal check
        for r in range(6):
            for c in range(4):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True
            
        # Vertical check
        for c in range(7):
            for r in range(3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

        # Positive Diagonal check
        for r in range(3):
            for c in range(4):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

        # Negative diagonal check 
        for r in range(3, 6):
            for c in range(4):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True

        return False

    def evaluate_window(self, window, piece):
        score = 0
        opponent_piece = 1
        if piece == 1:
            opponent_piece = 2

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 10
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 5
        if window.count(opponent_piece) == 3 and window.count(0) == 1:
            score -= 80

        return score

    def score_position(self, board, piece):
        score = 0

        center_list = [board[r][3] for r in range(6)]
        center_count = center_list.count(piece)
        score += center_count * 3

        # Horizontal check
        for r in range(6):
            for c in range(4):
                window = [board[r][c], board[r][c+1], board[r][c+2], board[r][c+3]]
                score += self.evaluate_window(window, piece)

        # Vertical check
        for c in range(7):
            for r in range(3):
                window = [board[r][c], board[r+1][c], board[r+2][c], board[r+3][c]]
                score += self.evaluate_window(window, piece)

        # Positive Diagonal check
        for r in range(3):
            for c in range(4):
                window = [board[r][c], board[r+1][c+1], board[r+2][c+2], board[r+3][c+3]]
                score += self.evaluate_window(window, piece)

        # Negative diagonal check 
        for r in range(3, 6):
            for c in range(4):
                window = [board[r][c], board[r-1][c+1], board[r-2][c+2], board[r-3][c+3]]
                score += self.evaluate_window(window, piece)

        return score

    def get_valid_location(self, board):
        valid_col = []
        for col in range(7):
            if self.Is_move_valid(board, col):
                valid_col.append(col)
        return valid_col

    def is_terminal_node(self, board):
        return (
            self.winning_move(board, 1) or
            self.winning_move(board, 2) or
            len(self.get_valid_location(board)) == 0
        )

    def minimax_algo(self, board, depth, maximizingPlayer):
        valid_locations = self.get_valid_location(board)
        terminal = self.is_terminal_node(board)

        # BASE CASE
        if depth == 0 or terminal:
            if self.winning_move(board, 2):
                return (None, 1000000)
            elif self.winning_move(board, 1):
                return (None, -1000000)
            elif len(valid_locations) == 0:
                return (None, 0)
            else:
                return (None, self.score_position(board, 2))

        # MAXIMIZING PLAYER (AI)
        if maximizingPlayer:
            best_score = -math.inf
            best_col = valid_locations[0]
            for col in valid_locations:
                temp_board = copy.deepcopy(board)
                self.Do_move(temp_board, col, 2)
                new_score = self.minimax_algo(temp_board, depth - 1, False)[1]
                if new_score > best_score:
                    best_score = new_score
                    best_col = col
            return best_col, best_score

        # MINIMIZING PLAYER (Human)
        else:
            best_score = math.inf
            best_col = valid_locations[0]
            for col in valid_locations:
                temp_board = copy.deepcopy(board)
                self.Do_move(temp_board, col, 1)
                new_score = self.minimax_algo(temp_board, depth - 1, True)[1]
                if new_score < best_score:
                    best_score = new_score
                    best_col = col
            return best_col, best_score


# ----------------------------------------------------------------
#  COLOR THEME  (AI / Cyberpunk-Tech)
# ----------------------------------------------------------------
BG         = "#0a0e1a"
BOARD_BG   = "#0d1b2a"
GRID_LINE  = "#1a2744"
EMPTY_CLR  = "#0f1e30"
PLAYER_CLR = "#00e5ff"   # cyan  — Human (piece 1)
AI_CLR     = "#ff3d71"   # neon pink-red — AI (piece 2)  
HOVER_CLR  = "#1e3a5f"
BTN_BG     = "#112240"
BTN_HOV    = "#1a3560"
ACCENT     = "#00e5ff"
TEXT_MAIN  = "#e0f0ff"
TEXT_DIM   = "#4a6fa5"

ROWS   = 6
COLS   = 7
CELL   = 80
RADIUS = 30
PAD    = 20
DEPTH  = 4


# ----------------------------------------------------------------
#  GUI CLASS
# ----------------------------------------------------------------
class Connect4GUI:

    def __init__(self, root):
        self.root      = root
        self.root.title("Connect-4  •  AI Edition")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.game        = Connect_4_Game()
        self.board       = self.game.create_board()
        self.game_over   = False
        self.hover_col   = -1
        self.player_turn = True   # True = human's turn, False = AI's turn

        self._build_ui()
        self._draw_board()

    # ── UI Layout ───────────────────────────────────────────────

    def _build_ui(self):
        # Title
        top = tk.Frame(self.root, bg=BG)
        top.pack(pady=(20, 2))
        tk.Label(top, text="⬡  CONNECT-4", bg=BG, fg=ACCENT,
                 font=("Courier New", 22, "bold")).pack()
        tk.Label(top, text="Minimax AI  •  Depth 4",
                 bg=BG, fg=TEXT_DIM, font=("Courier New", 10)).pack()

        # Legend
        leg = tk.Frame(self.root, bg=BG)
        leg.pack(pady=(8, 0))
        self._dot(leg, PLAYER_CLR, " YOU (Piece 1) ")
        tk.Label(leg, text="vs", bg=BG, fg=TEXT_DIM,
                 font=("Courier New", 11)).pack(side=tk.LEFT, padx=6)
        self._dot(leg, AI_CLR, " AI  (Piece 2) ")

        # Status
        self.status_var = tk.StringVar(value="Your turn  —  click a column")
        self.status_lbl = tk.Label(
            self.root, textvariable=self.status_var,
            bg=BG, fg=TEXT_MAIN, font=("Courier New", 12, "bold"), pady=8)
        self.status_lbl.pack()

        # Canvas
        cw = COLS * CELL + 2 * PAD
        ch = ROWS * CELL + 2 * PAD
        self.canvas = tk.Canvas(
            self.root, width=cw, height=ch,
            bg=BOARD_BG, highlightthickness=2,
            highlightbackground=ACCENT)
        self.canvas.pack(padx=24, pady=4)

        self.canvas.bind("<Motion>",   self._on_hover)
        self.canvas.bind("<Button-1>", self._on_click)
        self.canvas.bind("<Leave>",    self._on_leave)

        # Buttons
        btn_row = tk.Frame(self.root, bg=BG)
        btn_row.pack(pady=(6, 20))
        self._btn(btn_row, "⟳  New Game", self._new_game).pack(side=tk.LEFT, padx=10)
        self._btn(btn_row, "✕  Quit",     self.root.destroy).pack(side=tk.LEFT, padx=10)

    def _dot(self, parent, color, label):
        c = tk.Canvas(parent, width=16, height=16, bg=BG, highlightthickness=0)
        c.pack(side=tk.LEFT)
        c.create_oval(2, 2, 14, 14, fill=color, outline=color)
        tk.Label(parent, text=label, bg=BG, fg=color,
                 font=("Courier New", 11, "bold")).pack(side=tk.LEFT)

    def _btn(self, parent, text, cmd):
        return tk.Button(
            parent, text=text, command=cmd,
            bg=BTN_BG, fg=TEXT_MAIN,
            activebackground=BTN_HOV, activeforeground=ACCENT,
            relief=tk.FLAT, font=("Courier New", 11, "bold"),
            padx=14, pady=6, cursor="hand2",
            borderwidth=1, highlightthickness=1,
            highlightbackground=ACCENT)

    # ── Board Drawing ────────────────────────────────────────────

    def _draw_board(self):
        self.canvas.delete("all")

        # Hover column highlight
        if 0 <= self.hover_col < COLS and not self.game_over and self.player_turn:
            x0 = PAD + self.hover_col * CELL
            self.canvas.create_rectangle(
                x0, PAD, x0 + CELL, PAD + ROWS * CELL,
                fill=HOVER_CLR, outline="")

        # Grid lines
        for r in range(ROWS + 1):
            y = PAD + r * CELL
            self.canvas.create_line(PAD, y, PAD + COLS * CELL, y,
                                    fill=GRID_LINE, width=1)
        for c in range(COLS + 1):
            x = PAD + c * CELL
            self.canvas.create_line(x, PAD, x, PAD + ROWS * CELL,
                                    fill=GRID_LINE, width=1)

        # Discs
        for r in range(ROWS):
            for c in range(COLS):
                cx = PAD + c * CELL + CELL // 2
                cy = PAD + r * CELL + CELL // 2
                val = self.board[r][c]

                if val == 1:
                    fill, ring = PLAYER_CLR, PLAYER_CLR
                elif val == 2:
                    fill, ring = AI_CLR, AI_CLR
                else:
                    fill, ring = EMPTY_CLR, GRID_LINE

                self.canvas.create_oval(
                    cx - RADIUS, cy - RADIUS,
                    cx + RADIUS, cy + RADIUS,
                    fill=fill, outline=ring, width=2)



        # Column numbers
        for c in range(COLS):
            cx = PAD + c * CELL + CELL // 2
            self.canvas.create_text(
                cx, PAD + ROWS * CELL + 12,
                text=str(c), fill=TEXT_DIM,
                font=("Courier New", 9))

    # ── Mouse Events ─────────────────────────────────────────────

    def _col_from_x(self, x):
        if x < PAD or x > PAD + COLS * CELL:
            return -1
        return (x - PAD) // CELL

    def _on_hover(self, event):
        if self.game_over or not self.player_turn:
            return
        col = self._col_from_x(event.x)
        if col != self.hover_col:
            self.hover_col = col
            self._draw_board()

    def _on_leave(self, event):
        self.hover_col = -1
        self._draw_board()

    def _on_click(self, event):
        if self.game_over or not self.player_turn:
            return
        col = self._col_from_x(event.x)
        if col < 0:
            return
        self._do_player_turn(col)

    # ── Game Flow ────────────────────────────────────────────────

    def _do_player_turn(self, col):
        if not self.game.Is_move_valid(self.board, col):
            self.status_var.set("⚠  Column full — pick another")
            return

        # Place human disc (piece 1)
        self.game.Do_move(self.board, col, 1)
        self._draw_board()

        if self.game.winning_move(self.board, 1):
            self._end_game("🎉  You Win!", PLAYER_CLR)
            return

        if len(self.game.get_valid_location(self.board)) == 0:
            self._end_game("🤝  It's a Draw!", TEXT_DIM)
            return

        # Lock clicks, show thinking message, then run AI after short delay
        self.player_turn = False
        self.status_var.set("⚙  AI is thinking...")
        self.root.update()
        self.root.after(300, self._do_ai_turn)

    def _do_ai_turn(self):
        # Call YOUR original minimax_algo
        ai_col, ai_score = self.game.minimax_algo(self.board, DEPTH, True)

        if ai_col is not None and self.game.Is_move_valid(self.board, ai_col):
            self.game.Do_move(self.board, ai_col, 2)

        self._draw_board()

        if self.game.winning_move(self.board, 2):
            self._end_game("🤖  AI Wins!", AI_CLR)
            return

        if len(self.game.get_valid_location(self.board)) == 0:
            self._end_game("🤝  It's a Draw!", TEXT_DIM)
            return

        # Give control back to human
        self.player_turn = True
        self.status_var.set("Your turn  —  click a column")

    def _end_game(self, message, color):
        self.game_over = True
        self.hover_col = -1
        self._draw_board()
        self.status_lbl.config(fg=color)
        self.status_var.set(message)

    def _new_game(self):
        self.board       = self.game.create_board()
        self.game_over   = False
        self.player_turn = True
        self.hover_col   = -1
        self.status_lbl.config(fg=TEXT_MAIN)
        self.status_var.set("Your turn  —  click a column")
        self._draw_board()

#  ENTRY POINT
if __name__ == "__main__":
    root = tk.Tk()
    Connect4GUI(root)
    root.mainloop()