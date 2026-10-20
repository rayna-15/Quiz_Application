# Python Quiz Application

## Project Description
A beginner-friendly, menu-driven quiz application written in Python. Players can choose a topic category, answer multiple-choice questions, see explanations, and review a top-10 leaderboard.

## Features
- Categories: Python (20 questions), Computers (10 questions), Science (10 questions), and General Knowledge (10 questions)
- Randomized question order
- Selectable question count
- Per-question elapsed-time limit (checked when the player submits an answer)
- Score and percentage calculation
- Answer explanations
- Results saved to JSON files
- Top-10 leaderboard
- Input validation and file-error handling
- Object-oriented design using classes and methods

## Technologies Used
- Python 3
- Built-in modules: `json`, `random`, `time`, `datetime`, `pathlib`

## Python Concepts Used
Variables and data types, input/output, type casting, conditional statements, loops, functions/methods, lists, dictionaries, sets, file handling, exception handling, classes and objects, constructors, and basic encapsulation through class methods.

## Installation / Setup
1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open a terminal in the project folder.

## How to Run
```bash
python main.py
```
On some Windows installations, use:
```bash
py main.py
```

No third-party packages are required.

## How to Play
1. Choose **Start Quiz**.
2. Enter a player name.
3. Choose a category or all categories.
4. Select the number of questions.
5. Set a time limit between 5 and 60 seconds.
6. Answer using A, B, C, or D.
7. View your score and the leaderboard.

## Project Files
- `main.py` — application source code
- `quiz_results.json` — generated history of quiz attempts
- `leaderboard.json` — generated top-10 leaderboard
- `screenshots/` — screenshots for documentation

## Future Improvements
- Add a graphical interface with Tkinter.
- Add an admin option to create questions.
- Add more categories and difficulty levels.
- Use a database for users and quiz history.
- Add a true live countdown timer using a GUI or asynchronous input.

## Note About the Timer
This terminal version measures the time taken to submit each answer and checks it after Enter is pressed. It does not interrupt keyboard input exactly when the time limit expires. A GUI version could implement a live countdown.


## Question Bank
The application includes 50 multiple-choice questions across Python (20 questions), Computers (10 questions), Science (10 questions), and General Knowledge (10 questions).
