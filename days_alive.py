
from datetime import date, timedelta
import datetime

answer_year =int(input("What year were you born in? "))
answer_month = int(input("What month were you born in? "))
answer_day = int(input("What day were you born on? "))

today = date.today()

birthdate = date(answer_year, answer_month, answer_day)
dif = today - birthdate

print(f"You were born {dif.days} days ago")

end_date = birthdate + datetime.timedelta(days = 10000)

print(f"You will be 10000 days old on {end_date}")