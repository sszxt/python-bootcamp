small_pizza = 15
medium_pizza = 20
big_pizza = 25
pepporini = 2 # M or L means 3
extra_cheese = 1
bill = 0

print("welcome to pizza shop!")

pizza = input("what is your pizza?")
if pizza == "S":
    bill = small_pizza
elif pizza == "M":
    bill = medium_pizza
elif pizza == "B":
    bill = big_pizza

wants_pepporini = input("do you want pepporini? Y/N")
if wants_pepporini == "Y":
    bill += pepporini
elif pizza == "medium" or pizza == "big":
    bill += pepporini + 1

wants_cheese = input("do you want cheese? Y/N")
if wants_cheese == "Y":
    bill += extra_cheese

print(f"your bill is: {bill}")
