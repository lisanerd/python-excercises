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
    

    question = f'''Q) What is {random_number_1} {random_sign} {random_number_2}?'''
    return question, answer

class Test:
    def __init__(self, nbr_questions: int) -> None:
        self.question_list = [math_question() for _ in range(nbr_questions)]
        self.score: int = 0
        self.wrong_answers = []

    def start(self):
        total_points = 0
        for question, answer in self.question_list:
            print(question)
            u_a = self.ask_the_user()

            if answer == u_a:
                total_points += 1
            else:
                self.wrong_answers.append([question, answer, u_a])

        self.final_score = (total_points/5) * 100

    def debrief(self):
        print(f'Your final score is {str(self.final_score)}%')
        print("You got these questions wrong: ")
        for question, answer, u_a in self.wrong_answers:
            print(f"For the question {question}, you answered {u_a}, but the correct answer was {answer}.")
        

    def ask_the_user(self):
        user_answer = input("Enter your answer here: ")
        try:
            return int(user_answer)
        except:
            print("This is not a number you poopyhead.")
            return self.ask_the_user()
        


my_test = Test(nbr_questions=5)
my_test.start()
my_test.debrief()
