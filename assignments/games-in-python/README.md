# 📘 Assignment: Games in Python — Hangman

## 🎯 Objetivos

Build the classic Hangman word-guessing game using Python strings, loops, conditionals, and user input. Focus on clean input handling, state tracking, and user feedback.

## 📝 Tarefas

### 🛠️ Hangman Core Game

#### Description
Implement a playable Hangman game that selects a random word, accepts letter guesses, and tracks progress until the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Accept single-letter guesses and show current progress (e.g., `_ _ a _ _`).
- Track and display the number of incorrect guesses remaining.
- End the game when the word is fully guessed or attempts are exhausted.
- Display clear win/lose messages.

Example session:
```
Word: _ _ _ _ _
Attempts left: 6
Guess a letter: a
Word: a _ _ _ _
Attempts left: 6
Guess a letter: z
Word: a _ _ _ _
Attempts left: 5
...
```

### 🛠️ Enhancements (Optional)

#### Description
Improve the player experience and robustness with additional features.

#### Requirements
Completed program should:

- Show letters already guessed and prevent duplicate guesses.
- Validate input (single alphabetic character only).
- Optionally add simple ASCII art or difficulty levels.

