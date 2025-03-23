
# 🎮 Dooz - Single Player (Tic-Tac-Toe)

![Tic Tac Toe](https://upload.wikimedia.org/wikipedia/commons/3/32/Tic_tac_toe.svg)


This project is a single-player Tic-Tac-Toe (Dooz) game where the player competes against the computer.

## 📌 Features
- Single-player game against the system
- Beautiful game board display using `tabulate`
- Random selection of the first player
- Win checking and option for replay
- Written in **Python**

## 🚀 How to Run

### 1️⃣ **Prerequisites**

Before running the game, install Python and the required libraries.

```bash
pip install tabulate
```

### 2️⃣ **Run the Game**

```bash
python Dooz-Single-Player.py
```

## 🎯 How to Play
- Player 1 chooses between `X` or `O`.
- Players take turns selecting a position (1-9).
- The system randomly selects a position.
- If a player places three marks in a row (horizontal, vertical, or diagonal), they win.
- **Replay option** is available after each round.

## 🛠 Technologies Used
- **Python**
- **Tabulate** (for a better table display)

## 📝 Code Explanation

### 1️⃣ **Importing Libraries**
- `os`: For executing system commands (e.g., clearing the screen).
- `random`: For random selection of the first player and system moves.
- `tabulate`: For displaying the game board in a structured format.
- `clear_output`: To clear previous output (mainly for Jupyter Notebook environments).

### 2️⃣ **Initializing Variables**
- `playerNumber`: Determines whose turn it is (`0` for Player 1, `1` for the system).
- `gameTable`: The game board initialized with position numbers.
- `systemPlayerChoices`: A list of available positions for the system to select from.

### 3️⃣ **Main Functions**
- `PlayerInput()`: Gets the player's choice of `X` or `O`.
- `PlayerChoise()`: Gets the player's move.
- `PlaceMarker(board, marker, position)`: Places a move on the board.
- `PrintGameTable()`: Displays the current game board.
- `WinCheck(board, marker)`: Checks if a player has won by verifying rows, columns, and diagonals.
- `ChooseFirst()`: Randomly selects the first player.
- `SpaceCheck(board, position)`: Checks if a position is available.
- `FullBoardCheck(board)`: Checks if the board is full.
- `Replay()`: Asks the user if they want to play again.

### 4️⃣ **Game Loop Execution**
- The game runs in an infinite loop (`while True`).
- The board is reset, and players are selected.
- Players take turns making moves.
- The game ends if a player wins or if the board is full, with the option to restart.

## 📜 License
This project is released under the **MIT License**. You are free to use and modify it.

## 🤝 Contributions
If you have suggestions or want to contribute:
1. **Fork** this repository.
2. Make your changes.
3. Submit a **Pull Request**!

🌟 **If you like this project, give it a star on GitHub!** ⭐


📌 **Author:** Peiman Daii Rezaei  
📅 **Release Date:** March 2025

