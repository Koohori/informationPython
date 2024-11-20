import random


sum = 0
count_even = 0
largest = 0

for i in range (1,5):
    result = random.randint(1,7)
    print(f'roll was {result}')
    sum += result
    if result % 2 == 0:
        count_even += 1
    if result >= largest:
        largest = result

print(f'the sum of the outcome was {sum}, the number of times an even number was rolled was {count_even}, and the largest number was {largest}.')
