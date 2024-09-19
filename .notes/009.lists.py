# fruits = ["Cherry", "Apple", "Pear"]

# fruits[0] = "Lime"

# fruits.append("Grape")

# fruits.extend(["Pineapple", "Lemon"])

# print(fruits)

# Randomization plus lists usecase

import random
friends = ["Alice", "Bob", "Charlie","David", "Emanuel"]

random_int = random.randint(0, 4)

who_pays = friends[random_int]

print(f"{who_pays} will pay today.")

# Another way to do this:

print(random.choice(friends))

print(len(friends))

