print("Welcome to Moaz's Pizzeria!")
size=input("What size would you like? S, M, or L:")
pepperoni=input("Would you like pepperoni on your pizza? Y or N:")
extra_cheese=input("Would you like extra cheese on your pizza? Y or N:")
olives=input("Would you like olives on your pizza? Y or No:")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Recheck what you typed bro :(")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3
if extra_cheese == "Y":
    bill += 1
if olives == "Y":
    bill += 4
print(f"Your final bill is ${bill}. Enjoy :).....Fatty o_o")
