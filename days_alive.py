
from datetime import date

answer_year =int(input("What year were you born in? "))
answer_month = int(input("What month were you born in? "))
answer_day = int(input("What day were you born on? "))

def num_of_days(answer:int, date_2):
    return(date_2 - answer)

today = date.today()

date_1 = date(answer_year, answer_month, answer_day)
date_2 = today
dif = num_of_days(date_1, date_2)

print(f"You were born {dif.days} days ago")