import random


def math_question():
    random_number_1 = random.randint(1, 20)
    random_number_2 = random.randint(1, 20)
    random_sign = random.sample(['-', '+', '/', '*'], k=1)[0]

    if random_sign == '+':
        answer = random_number_1 + random_number_2
    if random_sign == '-':
        answer = random_number_1 - random_number_2
    if random_sign == '/':
        answer = random_number_1
        random_number_1 = random_number_1 * random_number_2
    if random_sign == '*':
        answer = random_number_1 * random_number_2
    

    question = f'''Q) What is {random_number_1} {random_sign} {random_number_2} ?'''
    return question, answer


question_list = [math_question(), math_question(), math_question(), math_question(), math_question()]

def ask_the_user():
    while True:
        user_answer = input("Enter your answer here: ")
        return int(user_answer)
        
total_points = 0
for question, answer in question_list:
    print(question)
    u_a = ask_the_user()

    if answer == u_a:
        total_points += 1

final_score = (total_points/5) * 100
print(f'Your final score is {str(final_score)}%')