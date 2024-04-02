print ("Welcome to the tip calculator!")
bill = float(input("What was the total bill?: $"))
tip = int(input("How much tip % would you like to give?: "))
split = int(input("How many people to split the bill?: "))

#Math
bill_with_tip = (tip / 100 * bill) + bill
bill_per_person = bill_with_tip / split
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person) #Format to show 0 after decimal. Normally would display as 33.6 now it displays 33.60.

print (f"Each person should pay: ${final_amount}")