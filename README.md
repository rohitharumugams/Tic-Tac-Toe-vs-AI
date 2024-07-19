# Tic Tac Toe vs AI

## Overview

This is a simple Tic Tac Toe game created using Pygame. The twist is that you play against an AI that uses the Minimax algorithm to ensure it never loses. Either you lose, or the game ends in a tie.

## Features

- Play against an unbeatable AI
- Clean and simple UI
- Restart the game anytime by pressing the 'R' key

## Minimax Algorithm

The AI uses the Minimax algorithm to make its moves. The algorithm works as follows:

1. **Simulates all possible moves** the AI can make and all possible responses from the opponent (you).
2. **Evaluates the game board** after each move to determine if it's a winning, losing, or draw position.
3. **Recursive Evaluation**: Evaluates the game tree from the current move until the end of the game, assigning scores to each possible move: +1 for a win, -1 for a loss, and 0 for a draw.
4. **Selects the move with the highest score**, ensuring it never loses.

## Future Improvements

In the next version, I plan to add a 20% probability that the AI might "miss" the optimal Minimax move and make a blunder, just like humans sometimes do, to make the game more enjoyable and fair.

Edit: 19/07/2024
Added a 20% probability for the AI to make a blunder.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-ai.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tic-tac-toe-ai
   ```
3. Install the required dependencies:
   ```bash
   pip install pygame numpy
   ```

## Usage

1. Run the game:
   ```bash
   python main.py
   ```
2. Click on the grid to make your move.
3. Press 'R' to restart the game.

## Acknowledgements

This project was inspired by the [NeuralNine](https://www.youtube.com/watch?v=LbTu0rwikwg) channel on YouTube.

## Contributing

Feel free to fork this project and submit pull requests. If you have any suggestions or improvements, please open an issue or reach out to me.
