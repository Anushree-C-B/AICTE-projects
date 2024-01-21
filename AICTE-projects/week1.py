class QuizGame:
    def __init__(self):
       # Initialize the quiz with a list of dictionaries containing questions, options, and correct answers
        self.questions = [
            {
                'question': 'What is the capital of France?',
                'options': ['A. Berlin', 'B. Paris', 'C. Rome', 'D. Madrid'],
                'correct_answer': 'B'
            },
            {
                'question': 'Which planet is known as the Red Planet?',
                'options': ['A. Venus', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
                'correct_answer': 'B'
            },
            {
                'question': 'What is the largest mammal?',
                'options': ['A. Elephant', 'B. Blue Whale', 'C. Giraffe', 'D. Gorilla'],
                'correct_answer': 'B'
            }
            # Add more questions as needed
        ]
        self.score = 0 # Initialize the player's score

    def display_question(self, question_data):
      # Display the question and options, and prompt the user for an answer
        print(question_data['question'])
        for option in question_data['options']:
            print(option)
        user_answer = input('Your answer (Enter A, B, C, or D): ')
        return user_answer.upper()

    def check_answer(self, user_answer, correct_answer):
       # Check if the user's answer is correct and provide feedback
        if user_answer == correct_answer:
            print('Correct!\n')
            self.score += 1 # Increase the score if the answer is correct
        else:
            print(f'Incorrect. The correct answer is {correct_answer}.\n')

    def play_quiz(self):
        print('Welcome to the Quiz Game!\n')
        for question_data in self.questions:
            user_answer = self.display_question(question_data)
            self.check_answer(user_answer, question_data['correct_answer'])
        # Display the final score at the end of the quiz
        print(f'Quiz completed! Your score is {self.score}/{len(self.questions)}.')


if __name__ == "__main__":
    quiz = QuizGame()# Create an instance of the QuizGame class
    quiz.play_quiz()# To start the game
