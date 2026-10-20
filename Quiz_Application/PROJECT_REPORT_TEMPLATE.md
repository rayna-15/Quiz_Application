# Week 6 Final Project Report: Python Quiz Application

## Student Details
- **Student Name:** Rayna
- **Internship Domain:** Python Development
- **Week:** 6 of 6

## 1. Project Introduction
The Python Quiz Application is a menu-driven program that asks multiple-choice questions and calculates a player's score. It includes topic categories, randomized questions, an answer-time limit, result storage, and a leaderboard.

## 2. Problem Statement
Learners need a simple way to practice general and programming knowledge and receive immediate feedback on their answers. This project provides a terminal-based quiz and records results for later review.

## 3. Objectives
- Build a working quiz using Python.
- Use OOP concepts to organize questions and quiz behaviour.
- Validate user input and handle missing or invalid data files.
- Calculate scores and percentages.
- Save quiz attempts and display a leaderboard.
- Upload and document the project on GitHub.

## 4. Features
- Four question categories.
- Random question order.
- Multiple-choice answers.
- Per-question elapsed-time checking.
- Immediate feedback and explanations.
- Score and percentage calculation.
- JSON file storage for results and leaderboard.
- Top-10 leaderboard.
- Input validation and menu navigation.

## 5. Technologies Used
Python 3 and its built-in `json`, `random`, `time`, `datetime`, and `pathlib` modules. No external packages are required.

## 6. Python Concepts Implemented
- Variables and data types for player details, answers, scores, and timing.
- Input/output for the menu and quiz interaction.
- Type casting and validation for question count and time limit.
- Conditional statements for menu choices and answer checking.
- Loops to display questions and keep the menu running.
- Classes, objects, constructors, and methods.
- Lists, dictionaries, and sets for questions and results.
- File handling using JSON files.
- Exception handling for invalid input and missing/corrupt JSON files.
- Git/GitHub for version control and repository hosting.

## 7. Project Workflow
1. The application displays the main menu.
2. The player starts a quiz and enters a name.
3. The player selects a category, number of questions, and time limit.
4. Questions are shuffled and shown one by one.
5. The program checks answers and displays explanations.
6. The final score and percentage are calculated.
7. Results are saved to `quiz_results.json` and `leaderboard.json`.
8. The player can view the leaderboard or start another quiz.

## 8. Source Code Explanation
- `Question` class stores the category, question text, options, correct answer, and explanation.
- `QuizApplication` class contains the quiz questions and all application operations.
- `choose_category()` validates and returns the selected topic.
- `ask_question()` displays a question, checks elapsed time and answer, and returns the result.
- `run_quiz()` conducts a quiz and calculates the final score.
- `load_json()` and `save_json()` read and write result files safely.
- `show_leaderboard()` displays the top quiz attempts.
- `run()` manages the main menu.

## 9. Output Screenshots
Insert actual screenshots captured from VS Code:
1. Main menu
2. Category selection
3. Questions and answer feedback
4. Final score
5. Leaderboard
6. JSON result files (optional)

## 10. Challenges Faced
- Validating menu choices and numeric input.
- Keeping quiz questions and result records organized.
- Handling missing or invalid JSON files.
- Sorting leaderboard results consistently.
- Measuring answer time in a terminal application.

## 11. Future Improvements
A graphical interface, live countdown timer, additional question sets, difficulty levels, user profiles, and database storage could be added in the future.

## 12. Conclusion
The project applies core Python programming and OOP concepts to a practical quiz system. It demonstrates input validation, reusable methods, file handling, exception handling, score calculation, and project documentation.

## GitHub Repository Link
Add your repository URL here after pushing the project to GitHub.
