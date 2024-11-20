import random

sum = 0

for i in range(1,5):
    dice=random.randint(1,7)
    print(dice)
    sum += dice

print(sum)











'''
count = 0
sum = 0

for i in range (3,99):
    if i%2==1 and i%5==0:
        count +=1
        sum += i

        print(f'curently at {i} count is {count} and the sum is {sum}')




num = int(input('enter number: '))
total = 0
for i in range(1,num):
        total += i
print(total)


for i in range(11,32):
    if i%2==0:
        print(3*i)
'''
