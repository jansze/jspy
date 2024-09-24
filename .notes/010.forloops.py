# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# total_exam_score = sum(student_scores)
# max_score = 0

# for score in student_scores:
#     if score > max_score:
#         max_score = score
        
# print(max_score)

for number in range(1, 101):
    if number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 5 == 0 and number % 3 == 0:
        print("fizzbuzz")
    else:
        print(number)