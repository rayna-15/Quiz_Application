import json
import random
import time
from datetime import datetime
from pathlib import Path


class Question:
    """Stores one multiple-choice question."""
    def __init__(self, category, prompt, options, answer, explanation):
        self.category = category
        self.prompt = prompt
        self.options = options
        self.answer = answer
        self.explanation = explanation


class QuizApplication:
    """Runs quizzes, measures answer time, and stores a leaderboard."""

    def __init__(self):
        self.questions = [
            Question('Python', 'Which keyword defines a function in Python?', ['A. func', 'B. def', 'C. function', 'D. define'], 'B', 'Python uses the def keyword to define a function.'),
            Question('Python', 'Which data type stores True or False?', ['A. int', 'B. str', 'C. bool', 'D. list'], 'C', 'The bool type stores True or False values.'),
            Question('Python', 'Which symbol begins a single-line comment?', ['A. //', 'B. <!-- -->', 'C. #', 'D. **'], 'C', 'A # begins a single-line comment in Python.'),
            Question('Python', 'Which collection is ordered and changeable?', ['A. tuple', 'B. list', 'C. frozenset', 'D. string'], 'B', 'Lists are ordered and mutable collections.'),
            Question('Python', 'Which method adds one item to a list?', ['A. add()', 'B. insert_end()', 'C. append()', 'D. push()'], 'C', 'append() adds an item to the end of a list.'),
            Question('Python', 'What is the result of 3 ** 2?', ['A. 6', 'B. 8', 'C. 9', 'D. 5'], 'C', 'The ** operator performs exponentiation: 3 squared is 9.'),
            Question('Python', 'Which statement repeats code while a condition is true?', ['A. if', 'B. while', 'C. def', 'D. import'], 'B', 'A while loop repeats as long as its condition is true.'),
            Question('Python', 'Which keyword is used to create a class?', ['A. object', 'B. define', 'C. class', 'D. struct'], 'C', 'Python classes are declared with the class keyword.'),
            Question('Python', 'What does len("quiz") return?', ['A. 3', 'B. 4', 'C. 5', 'D. 0'], 'B', 'The string "quiz" contains four characters.'),
            Question('Python', 'Which mode opens a file for appending?', ['A. r', 'B. w', 'C. a', 'D. x'], 'C', 'The a mode appends content to an existing file.'),
            Question('Computers', 'What does CPU stand for?', ['A. Central Processing Unit', 'B. Computer Personal Unit', 'C. Central Program Utility', 'D. Control Power Unit'], 'A', 'CPU stands for Central Processing Unit.'),
            Question('Computers', 'Which device is mainly used to enter text?', ['A. Monitor', 'B. Keyboard', 'C. Speaker', 'D. Projector'], 'B', 'A keyboard is commonly used to enter text.'),
            Question('Computers', 'Which component is often called the computer’s brain?', ['A. Mouse', 'B. CPU', 'C. Printer', 'D. Scanner'], 'B', 'The CPU processes instructions and controls operations.'),
            Question('Computers', 'Which of these is an operating system?', ['A. Python', 'B. Windows', 'C. HTML', 'D. Google'], 'B', 'Windows is an operating system.'),
            Question('Computers', 'What does RAM mainly provide?', ['A. Temporary working memory', 'B. Permanent printing', 'C. Internet service', 'D. Power backup'], 'A', 'RAM temporarily stores data and programs in use.'),
            Question('Computers', 'Which device displays visual output?', ['A. Keyboard', 'B. Microphone', 'C. Monitor', 'D. Joystick'], 'C', 'A monitor displays text, images and video.'),
            Question('Computers', 'Which is an example of an input device?', ['A. Speaker', 'B. Printer', 'C. Mouse', 'D. Projector'], 'C', 'A mouse sends user actions to the computer.'),
            Question('Computers', 'What is the full form of USB?', ['A. Universal Serial Bus', 'B. United System Board', 'C. User Storage Box', 'D. Universal Software Base'], 'A', 'USB stands for Universal Serial Bus.'),
            Question('Computers', 'Which of these is a web browser?', ['A. Excel', 'B. Chrome', 'C. Python', 'D. Linux'], 'B', 'Google Chrome is a web browser.'),
            Question('Computers', 'Which unit is commonly used to measure file size?', ['A. Meter', 'B. Kilogram', 'C. Byte', 'D. Celsius'], 'C', 'Digital file sizes are measured in bytes and their multiples.'),
            Question('Science', 'Which planet is known as the Red Planet?', ['A. Venus', 'B. Jupiter', 'C. Mars', 'D. Mercury'], 'C', 'Mars is known as the Red Planet.'),
            Question('Science', 'What is the chemical formula for water?', ['A. CO2', 'B. O2', 'C. NaCl', 'D. H2O'], 'D', 'Water’s chemical formula is H2O.'),
            Question('Science', 'Which gas do plants absorb during photosynthesis?', ['A. Oxygen', 'B. Carbon dioxide', 'C. Helium', 'D. Hydrogen'], 'B', 'Plants use carbon dioxide during photosynthesis.'),
            Question('Science', 'What force pulls objects toward Earth?', ['A. Magnetism only', 'B. Friction', 'C. Gravity', 'D. Electricity'], 'C', 'Gravity attracts objects toward Earth.'),
            Question('Science', 'At sea level, water boils at approximately what temperature?', ['A. 0°C', 'B. 50°C', 'C. 100°C', 'D. 150°C'], 'C', 'At standard atmospheric pressure, water boils at about 100°C.'),
            Question('Science', 'Which organ pumps blood around the human body?', ['A. Lungs', 'B. Heart', 'C. Stomach', 'D. Kidney'], 'B', 'The heart pumps blood through the circulatory system.'),
            Question('Science', 'What is the nearest star to Earth?', ['A. Sirius', 'B. Polaris', 'C. The Sun', 'D. Vega'], 'C', 'The Sun is the nearest star to Earth.'),
            Question('Science', 'Which vitamin can the body make with sunlight exposure?', ['A. Vitamin A', 'B. Vitamin B12', 'C. Vitamin C', 'D. Vitamin D'], 'D', 'Sunlight helps the skin produce vitamin D.'),
            Question('Science', 'What is the basic unit of life?', ['A. Atom', 'B. Cell', 'C. Organ', 'D. Tissue'], 'B', 'The cell is the basic structural and functional unit of life.'),
            Question('Science', 'Which state of matter has a fixed volume but no fixed shape?', ['A. Solid', 'B. Liquid', 'C. Gas', 'D. Plasma only'], 'B', 'A liquid has a fixed volume and takes the shape of its container.'),
            Question('General Knowledge', 'How many days are there in a leap year?', ['A. 364', 'B. 365', 'C. 366', 'D. 367'], 'C', 'A leap year has 366 days.'),
            Question('General Knowledge', 'Which is the largest ocean on Earth?', ['A. Atlantic', 'B. Pacific', 'C. Indian', 'D. Arctic'], 'B', 'The Pacific Ocean is the largest ocean on Earth.'),
            Question('General Knowledge', 'Which language is widely used to style web pages?', ['A. HTML', 'B. SQL', 'C. CSS', 'D. Python'], 'C', 'CSS is used to style web pages.'),
            Question('General Knowledge', 'What is the capital of Japan?', ['A. Seoul', 'B. Beijing', 'C. Tokyo', 'D. Bangkok'], 'C', 'Tokyo is the capital of Japan.'),
            Question('General Knowledge', 'How many sides does a hexagon have?', ['A. Five', 'B. Six', 'C. Seven', 'D. Eight'], 'B', 'A hexagon has six sides.'),
            Question('General Knowledge', 'Which is the largest mammal?', ['A. African elephant', 'B. Blue whale', 'C. Giraffe', 'D. Great white shark'], 'B', 'The blue whale is the largest known mammal.'),
            Question('General Knowledge', 'Which currency is used in India?', ['A. Yen', 'B. Dollar', 'C. Rupee', 'D. Euro'], 'C', 'The Indian rupee is the currency of India.'),
            Question('General Knowledge', 'How many colours are traditionally listed in a rainbow?', ['A. Five', 'B. Six', 'C. Seven', 'D. Eight'], 'C', 'A traditional rainbow description lists seven colours.'),
            Question('General Knowledge', 'Which festival is widely known as the festival of lights in India?', ['A. Holi', 'B. Diwali', 'C. Eid', 'D. Baisakhi'], 'B', 'Diwali is commonly known as the festival of lights.'),
            Question('General Knowledge', 'Which sport uses a racket and a shuttlecock?', ['A. Tennis', 'B. Cricket', 'C. Badminton', 'D. Hockey'], 'C', 'Badminton is played with rackets and a shuttlecock.'),
            Question('Python', 'Which keyword handles an exception?', ['A. catch', 'B. except', 'C. error', 'D. handle'], 'B', 'Python uses except in a try/except exception-handling structure.'),
            Question('Python', 'Which built-in type stores key-value pairs?', ['A. list', 'B. tuple', 'C. dict', 'D. set'], 'C', 'A dictionary stores key-value pairs.'),
            Question('Python', 'What does input() return by default?', ['A. Integer', 'B. String', 'C. Boolean', 'D. List'], 'B', 'input() returns the entered text as a string.'),
            Question('Python', 'Which keyword imports a module?', ['A. include', 'B. using', 'C. import', 'D. require'], 'C', 'The import keyword makes module functionality available.'),
            Question('Python', 'Which method reads all text from an open file?', ['A. read()', 'B. write()', 'C. close()', 'D. append()'], 'A', 'read() reads the file content.'),
            Question('Python', 'What does a constructor commonly use as its method name in Python?', ['A. start()', 'B. __init__()', 'C. new()', 'D. create()'], 'B', '__init__() initializes a new object’s attributes.'),
            Question('Python', 'Which keyword refers to the current instance inside a method?', ['A. this', 'B. self', 'C. current', 'D. me'], 'B', 'By convention, self refers to the current object instance.'),
            Question('Python', 'Which collection automatically removes duplicate values?', ['A. list', 'B. tuple', 'C. set', 'D. string'], 'C', 'A set stores unique elements.'),
            Question('Python', 'Which module provides functions such as randint()?', ['A. random', 'B. pathlib', 'C. datetime', 'D. json'], 'A', 'The random module provides randint() and other random functions.'),
            Question('Python', 'Which OOP concept allows a child class to reuse parent-class features?', ['A. Looping', 'B. Inheritance', 'C. Indexing', 'D. Casting'], 'B', 'Inheritance allows a class to extend another class.'),
        ]
        self.results_file = Path(__file__).with_name("quiz_results.json")
        self.leaderboard_file = Path(__file__).with_name("leaderboard.json")

    def load_json(self, path, default):
        """Read JSON safely; return a default value if the file is missing or invalid."""
        try:
            with path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return default

    def save_json(self, path, data):
        """Save data to a JSON file."""
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def choose_category(self):
        categories = sorted({question.category for question in self.questions})
        print("\nChoose a category:")
        print("0. All categories")
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")

        while True:
            choice = input("Enter category number: ").strip()
            if choice == "0":
                return "All"
            if choice.isdigit() and 1 <= int(choice) <= len(categories):
                return categories[int(choice) - 1]
            print("Invalid choice. Please enter a listed number.")

    def ask_question(self, question, number, total, time_limit):
        print(f"\nQuestion {number}/{total} [{question.category}]")
        print(question.prompt)
        for option in question.options:
            print(option)

        start = time.monotonic()
        answer = input(f"Your answer (A/B/C/D, {time_limit}s limit): ").strip().upper()
        elapsed = time.monotonic() - start

        # Input-based timing is approximate: it checks the elapsed time after Enter.
        if elapsed > time_limit:
            print(f"Time limit exceeded ({elapsed:.1f}s). No point awarded.")
            return False, elapsed

        if answer not in {"A", "B", "C", "D"}:
            print("Invalid answer. Please enter A, B, C, or D.")
            return False, elapsed

        if answer == question.answer:
            print("Correct!")
            is_correct = True
        else:
            print(f"Incorrect. Correct answer: {question.answer}")
            is_correct = False

        print("Explanation:", question.explanation)
        return is_correct, elapsed

    def run_quiz(self):
        print("\n=== PYTHON QUIZ APPLICATION ===")
        name = input("Enter your name: ").strip()
        if not name:
            name = "Guest"

        category = self.choose_category()
        available = self.questions if category == "All" else [
            question for question in self.questions if question.category == category
        ]

        if not available:
            print("No questions are available in this category.")
            return

        random.shuffle(available)
        try:
            raw_count = input(f"How many questions? (1-{len(available)}): ").strip()
            count = int(raw_count)
            if not 1 <= count <= len(available):
                raise ValueError
        except ValueError:
            print("Invalid number. Using all available questions.")
            count = len(available)

        try:
            raw_limit = input("Time limit per question in seconds (5-60, default 15): ").strip()
            time_limit = 15 if not raw_limit else int(raw_limit)
            if not 5 <= time_limit <= 60:
                raise ValueError
        except ValueError:
            print("Invalid time limit. Using 15 seconds.")
            time_limit = 15

        selected = available[:count]
        score = 0
        total_time = 0.0
        print("\nQuiz started! Answer with A, B, C, or D.")
        for number, question in enumerate(selected, start=1):
            correct, elapsed = self.ask_question(question, number, len(selected), time_limit)
            score += int(correct)
            total_time += elapsed

        percentage = (score / len(selected)) * 100
        result = {
            "name": name,
            "category": category,
            "score": score,
            "total": len(selected),
            "percentage": round(percentage, 2),
            "time_seconds": round(total_time, 2),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        print("\n=== QUIZ RESULT ===")
        print(f"Player: {name}")
        print(f"Category: {category}")
        print(f"Score: {score}/{len(selected)}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Total answer time: {total_time:.1f} seconds")

        results = self.load_json(self.results_file, [])
        results.append(result)
        self.save_json(self.results_file, results)

        leaderboard = self.load_json(self.leaderboard_file, [])
        leaderboard.append(result)
        leaderboard.sort(key=lambda item: (item["score"] / item["total"], item["score"], -item["time_seconds"]), reverse=True)
        self.save_json(self.leaderboard_file, leaderboard[:10])
        print("Result saved successfully.")

    def show_leaderboard(self):
        leaderboard = self.load_json(self.leaderboard_file, [])
        print("\n=== TOP 10 LEADERBOARD ===")
        if not leaderboard:
            print("No results yet. Play a quiz first.")
            return

        for rank, result in enumerate(leaderboard, start=1):
            print(
                f"{rank}. {result['name']} | {result['score']}/{result['total']} "
                f"({result['percentage']:.1f}%) | {result['category']} | "
                f"{result['date']}"
            )

    def show_instructions(self):
        print("\nHOW TO PLAY")
        print("- Choose a category or all categories.")
        print("- Select how many questions to answer.")
        print("- Enter A, B, C, or D for each answer.")
        print("- Answer within the time limit for points.")
        print("- Your score is saved and can appear on the leaderboard.")

    def run(self):
        while True:
            print("\n" + "=" * 38)
            print("        PYTHON QUIZ APPLICATION")
            print("=" * 38)
            print("1. Start Quiz")
            print("2. View Leaderboard")
            print("3. Instructions")
            print("4. Exit")
            choice = input("Choose an option (1-4): ").strip()

            if choice == "1":
                self.run_quiz()
            elif choice == "2":
                self.show_leaderboard()
            elif choice == "3":
                self.show_instructions()
            elif choice == "4":
                print("Thank you for playing. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    QuizApplication().run()
