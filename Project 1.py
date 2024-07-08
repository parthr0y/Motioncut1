class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "category": "General Knowledge",
                "question": "What is the capital of France?",
                "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
                "answer": "C"
            },
            {
                "category": "General Knowledge",
                "question": "Which planet is known as the Red Planet?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
                "answer": "B"
            },
            {
                "category": "General Knowledge",
                "question": "What is the largest ocean on Earth?",
                "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
                "answer": "D"
            },
            {
                "category": "Sports",
                "question": "Which country won the FIFA World Cup in 2018?",
                "options": ["A. Brazil", "B. Germany", "C. Argentina", "D. France"],
                "answer": "D"
            },
            {
                "category": "Sports",
                "question": "How many players are there on a basketball team?",
                "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
                "answer": "A"
            },
            {
                "category": "Sports",
                "question": "Who holds the record for the most home runs in a single MLB season?",
                "options": ["A. Barry Bonds", "B. Hank Aaron", "C. Babe Ruth", "D. Mark McGwire"],
                "answer": "A"
            },
            {
                "category": "Entertainment",
                "question": "Who directed the movie 'Inception'?",
                "options": ["A. Christopher Nolan", "B. Steven Spielberg", "C. James Cameron", "D. Martin Scorsese"],
                "answer": "A"
            },
            {
                "category": "Entertainment",
                "question": "Which actor played the character of Harry Potter in the movie series?",
                "options": ["A. Elijah Wood", "B. Daniel Radcliffe", "C. Rupert Grint", "D. Tom Felton"],
                "answer": "B"
            },
            {
                "category": "Entertainment",
                "question": "What is the highest-grossing film of all time?",
                "options": ["A. Titanic", "B. Avatar", "C. Avengers: Endgame", "D. Star Wars: The Force Awakens"],
                "answer": "C"
            },
            {
                "category": "General Knowledge",
                "question": "Which element has the chemical symbol 'O'?",
                "options": ["A. Gold", "B. Oxygen", "C. Osmium", "D. Neon"],
                "answer": "B"
            }
        ]
        self.score = 0

    def ask_question(self, question_data):
        print(f"Category: {question_data['category']}")
        print(question_data["question"])
        for option in question_data["options"]:
            print(option)
        user_answer = input("Please enter the letter of your answer: ").upper()
        return user_answer

    def provide_feedback(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")

    def start_quiz(self):
        for question in self.questions:
            user_answer = self.ask_question(question)
            while user_answer not in ['A', 'B', 'C', 'D']:
                print("Invalid input. Please enter A, B, C, or D.")
                user_answer = input("Please enter the letter of your answer: ").upper()
            self.provide_feedback(user_answer, question["answer"])
            print()

        print(f"Quiz Over! Your final score is {self.score} out of {len(self.questions)}.")

if __name__ == "__main__":
    game = QuizGame()
    game.start_quiz()

