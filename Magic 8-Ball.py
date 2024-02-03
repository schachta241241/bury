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

    # Запрос вопроса у пользователя
    question = input("Задайте ваш вопрос: ")

    # Получение случайного ответа из списка
    answer = random.choice(answers)

    # Вывод ответа
    print(f"Шар судьбы говорит: {answer}")

# Запуск программы
magic_8_ball()
