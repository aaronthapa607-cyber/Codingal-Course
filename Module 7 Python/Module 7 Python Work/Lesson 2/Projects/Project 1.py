import keyword

person_name = input("Enter your name: ")
goal_name = input("Enter one skill you want to get better at: ")
target_month = input ("Enter the month you want to reach it by: ")
daily_minutes = 30

print("\nMY PERSONAL GOAL PLAN\n")

print("Name:", person_name,"\n")
print("Goal:", goal_name,"\n")
print("Target Month:", target_month,"\n")
print("Daily Practice:", daily_minutes, "minutes", "\n")
print("Status:", end=" ",)
print("Not started \n")
print("Reminder:", end=" - ")
print("Practice every day! \n")

print("In one sentence:")
print(person_name, "wants to get better at", goal_name.lower(), "by practising", daily_minutes, "minutes a day until", target_month + ". \n")
print(keyword.kwlist)
