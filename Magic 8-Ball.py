import random

def magic_8_ball():
    # Список возможных ответов от шара судьбы
    answers = [
        "Yes, definitely!",
        "Most likely",
        "Unpredictable, ask again later",
        "Hard to say",
        "Don't count on it",
        "Definitely no",
        "My sources say no",
        "Very doubtful"
    ]

# Asking the user for a question
question = input("Ask your question: ")

# Getting a random answer from the list
answer = random.choice(answers)

# Displaying the answer
print(f"The magic 8-ball says: {answer}")

# Running the program
magic_8_ball()

