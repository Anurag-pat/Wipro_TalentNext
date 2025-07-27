"""
MINI PROJECT 1
create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.
Sample Output: How far would you like to travel in miles? 2500 I suggest Super-Car to you destination
"""
distance=float(input("How far would you like to travel in mile? "))

if distance<3:
    suggestion="Bicycle"
elif distance<300:
    suggestion="Moter-Cycle"
else:
    suggestion="Super-Car"

print(f"I suggest {suggestion} to your destination")


"""
MINI PROJECT 2
Let's assume you are planning to use your python skills to build an App for Mobile.
You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
Write a python program that displays the answers to the following questions: How much does it cost to operate one server per day? How much does it cost to operate one server per week? How much does it cost to operate one server per month? How much days can I operate one server with $918?
"""


hourly_cost = 0.51

daily_cost = hourly_cost * 24
weekly_cost = daily_cost * 7
monthly_cost = daily_cost * 30 

budget = 918
days_with_budget = budget / daily_cost

print("Cost to operate one server:")
print(f"Per day: ${daily_cost:.2f}")
print(f"Per week: ${weekly_cost:.2f}")
print(f"Per month: ${monthly_cost:.2f}")
print(f"With ${budget}, you can operate one server for approximately {days_with_budget:.2f} days.")