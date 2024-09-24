# Defining a function

def my_function():
    print("hello")
    print("bye")

# Calling a function
my_function()
    
# FOR

# for items in list_of_items:
#     Do something to each item
    
# for number in range (a, b):
#     print(number)

# WHILE LOOPS

# while something_is_true:
#     # Do something repeatedly. When something becomes false, it will stop.
    
while at_goal() != True:
    if wall_in_front() != False and wall_on_right() != False:
        turn_left()
    elif wall_on_right() != True and right_is_clear() != False:
        turn_right()
        move()
    elif front_is_clear() != False:
        move()
    elif wall_in_front() != False and right_is_clear() != False:
        turn_right()
        move()
    
    
# While loop with negation.
    