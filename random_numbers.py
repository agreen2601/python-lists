# 1
import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

# 2
numbers_1_to_10 = range(1, 11)

for number in numbers_1_to_10:
    the_numbers_match = True

    if number == my_randoms:
            print(f'{number} is in the random list')


    for num in my_randoms:
        if num == number:
            print(f'{num} is in the random list')
