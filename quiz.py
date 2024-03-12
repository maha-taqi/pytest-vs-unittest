class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Define the list of questions
questions = [
    Question("Which is the biggest continent in the world?\n(a) Antarctica\n(b) Australia\n(c) Asia\n\n", "c"),
    Question("Which is the most spoken language in the world?\n(a) English\n(b) Spanish\n(c) French\n\n", "a"),
    Question("Who wrote 'Romeo and Juliet'?\n(a) Charles Dickens\n(b) William Shakespeare\n(c) J.K. Rowling\n\n", "b")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer not in ['a', 'b', 'c']:
            raise TypeError('Input must be either a, b, c')
        if answer.lower() == question.answer:
            score += 1
    return f"You got {score} out of {len(questions)} correct."


if __name__ == '__main__':
    print(run_quiz(questions))
