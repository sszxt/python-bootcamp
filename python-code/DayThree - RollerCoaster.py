print("Welcome to the rollercoaster!!!")
height = int(input("Please enter your height:"))
bill = 0
if height > 120:
    age = int(input("Please enter your age:"))
    if age > 18:
        bill = 7
    else:
        bill = 5

    wants_photo = input("Would you like to see a photo? (Y/N):")
    if wants_photo == "Y":
        bill += 5

    print(f"Your bill is: {bill}")
else:
    print("You are too short to ride!")