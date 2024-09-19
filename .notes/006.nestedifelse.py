height = int(input("What is your height ?: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age ?: "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Do you want a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")

# Second example

# print("Welcome to Python pizza delivery!")
# size = input("What size would you like ? : S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza ? Y or N: ")
# extra_cheese = input("Do you want extra cheese ? Y or N: ")
# bill = 0

# if size == "S":
#     bill += 15
# if size == "M":
#     bill += 20
# if size == "L":
#     bill += 25
    
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
        
# if extra_cheese == "Y":
#     bill += 1
    
# print(f"Your total is : ${bill}.")
    