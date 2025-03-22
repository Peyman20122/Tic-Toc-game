# Tic-Toc-game

![Tic Tac Toe](https://upload.wikimedia.org/wikipedia/commons/3/32/Tic_tac_toe.svg)

## 🎯 About the Project
This project is a text-based implementation of the **Tic Tac Toe** game written in **Python**, designed to be played in the console. It is a two-player game where players take turns placing **X** or **O** on a 3×3 grid to determine the winner.

## 🚀 Features
✅ Runs in the terminal (no GUI required)  
✅ Player 1 can choose between X or O  
✅ Neatly displays the game board using **tabulate**  
✅ Checks for win conditions, draws, and board status  
✅ Asks players if they want to play again  

## 🛠️ Installation and Execution
### 1️⃣ Prerequisites
To run this project, you must have **Python** installed. If you don't have it, download it here:  
🔗 [Download Python](https://www.python.org/downloads/)

You also need to install the `tabulate` module. Use the following command:
```bash
pip install tabulate
```

### 2️⃣ Running the Game
To start the game, run the **Dooz2.py** file:
```bash
python Dooz2.py
```

## 🎮 How to Play
1️⃣ Player 1 chooses **X** or **O**.  
2️⃣ Players take turns selecting a position (1–9).  
3️⃣ The game board updates and displays after each move.  
4️⃣ If a player aligns three of their marks in a row, column, or diagonal, they win.  
5️⃣ If all cells are filled with no winner, the game is a draw.  
6️⃣ At the end of each game, players are asked if they want to play again.

## 📝 Code Structure
📂 **Dooz2.py** – Main script containing functions:
- `PlayerInput()` → Gets the choice of X or O from Player 1
- `PlayerChoise()` → Gets the player's selected position
- `PlaceMarker(board, marker, position)` → Places the mark on the board
- `PrintGameTable()` → Displays the game board
- `WinCheck(board, marker)` → Checks if a player has won
- `FullBoardCheck(board)` → Checks if the board is full
- `Replay()` → Asks if players want to play again

## 📌 Suggested Improvements
🔹 Implement **OOP (Object-Oriented Programming)** for better game state management  
🔹 Create a GUI version using **Tkinter** or **Pygame**  
🔹 Add an AI opponent for single-player mode  
🔹 Implement save and resume functionality  

## 🤝 Contributing
If you'd like to contribute to this project, feel free to fork it and submit a Pull Request! 🚀
```bash
git clone https://github.com/username/tic-tac-toe.git
cd tic-tac-toe
```

## 📜 License
This project is licensed under the **MIT License**. Feel free to use and modify it! 🚀

---
📌 **Author:** Peyman Daei Rezaei  
📅 **Release Date:** March 2025

