import random

def generate_math_question(a, b):

    operators = ("+", "-", "*", "/")

    num1 = random.randint(a, b)

    num2 = random.randint(a, b)

    operator = random.choice(operators)
    # Убедимся что не будет деления на ноль
    if operator == "/" and num2 == 0:
        num2 = 1     # если это произошло то меняем ноль на один

    result = f"{num1} {operator} {num2}"

    return result

# Проверка ответа пользователя на правильность
def check_answer(expression, user_answer):
    try:
        correct_answer = eval(expression)
        return correct_answer == float(user_answer)
    except ValueError:
            return False
        
    
def math_quiz(number_of_questions):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0
    
    for i in range(number_of_questions):
        expression = (generate_math_question(1, 5))
        print(expression)
        user_answer = input("Решите пример:")

        if check_answer(expression, user_answer) == True:
             correct_answers += 1



    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    if correct_answers >= 8:
        print("Отлично! Вы получаете оценку A.")
    elif correct_answers >= 6:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")

# запустим тест
math_quiz(10)