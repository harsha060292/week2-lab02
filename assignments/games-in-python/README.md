# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game in Python while practicing strings, loops, user input, and game-state logic.

## 📝 Tasks

### 🛠️ Word Selection and Display

#### Description
Create a function that selects a secret word at random from a predefined list and initializes a masked progress display (e.g., `_ _ _ _`).

#### Requirements
Completed program should:

- Have a list of at least 10 words.
- Pick one word randomly using the `random` module.
- Represent hidden letters as underscores and reveal correct guesses in place.

### 🛠️ Guess Handling and Game Loop

#### Description
Implement the main game loop where the player can guess letters, track mistakes, and see progress updates.

#### Requirements
Completed program should:

- Accept letter input from the player each turn.
- Update the display for correct guesses and maintain a list of used letters.
- Track remaining wrong guess attempts (e.g., max 6 incorrect guesses).
- End the game with a win message when the word is fully guessed, or a lose message when attempts are exhausted.
- Show appropriate feedback after each guess (current state, wrong guesses left, and used letters).
