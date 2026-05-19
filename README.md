# Connect-4 — Minimax AI (Python + Tkinter)

A terminal-born Connect-4 game upgraded with a graphical interface, where you play against an AI powered by the **Minimax algorithm**.

---

## Features
- Clickable GUI board built with Python's built-in `tkinter` library
- AI opponent using Minimax with a search depth of 4
- Column hover highlight to guide your move
- Win / Draw detection with on-screen result message
- New Game button to restart without closing the app

---

## How to Run

**Requirements:** Python 3.x (tkinter is included by default)

```bash
python connect4_gui.py
```

No external libraries needed — pure Python standard library only.

---

## How to Play

| Action | What to do |
|---|---|
| Make a move | Click any column on the board |
| Restart | Click **⟳ New Game** |
| Quit | Click **✕ Quit** |

- You are **Piece 1** (Cyan)
- AI is **Piece 2** (Red)
- First to connect 4 in a row — horizontal, vertical, or diagonal — wins

---

## Project Structure

```
connect4_gui.py
│
├── Connect_4_Game        # Core game logic
│   ├── create_board()        - Initializes 6x7 board
│   ├── Is_move_valid()       - Validates column selection
│   ├── Do_move()             - Places a piece on the board
│   ├── winning_move()        - Checks all win conditions
│   ├── evaluate_window()     - Scores a 4-cell window
│   ├── score_position()      - Full board heuristic scoring
│   ├── get_valid_location()  - Returns playable columns
│   ├── is_terminal_node()    - Checks game-over state
│   └── minimax_algo()        - Minimax decision engine
│
└── Connect4GUI           # Tkinter GUI layer
    ├── _build_ui()           - Builds all widgets
    ├── _draw_board()         - Redraws board on canvas
    ├── _do_player_turn()     - Handles human move
    └── _do_ai_turn()         - Triggers and applies AI move
```

---

## AI — How Minimax Works

The AI uses the **Minimax algorithm** — a classical game-tree search technique used in two-player zero-sum games.

- The AI simulates all possible moves up to **depth 4**
- At each level it alternates between **maximizing** its own score (AI) and **minimizing** the player's advantage (Human)
- Board positions are scored using a **heuristic function** that rewards center control, 3-in-a-row threats, and penalizes opponent threats
- The AI always picks the column with the highest resulting score

---

## Known Limitation

The AI runs on the main thread. At depth 4, expect a **~0.5–1 second pause** while it thinks — this is normal behavior for a pure Minimax implementation without threading or Alpha-Beta pruning.

---

## Built With

- **Language:** Python 3
- **GUI:** tkinter (standard library)
- **Algorithm:** Minimax (no Alpha-Beta pruning)