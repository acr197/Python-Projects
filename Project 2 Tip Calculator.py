#Tip Calculator

print("Welcome to the Tip Calulator!\n")
total = float(input("What was the total bill?\n"))
percent = float(input("What % tip would you lke to give? 15, 20, or 25?\n"))
people = int(input("How many people are splitting the bill?\n"))

tip = round(total * (.01 * percent) / people,2)

print(f"Each person should pay ${tip}")