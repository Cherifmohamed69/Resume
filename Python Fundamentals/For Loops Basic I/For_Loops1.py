for i in range(151):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range(1, 101):
    if i % 5 == 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)

sum_of_odds = 0

for i in range(0, 500001):
    sum_of_odds += i

print(sum_of_odds )

numbers = 2018
while numbers > 0:
    print (numbers)
    numbers -=4

lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum+1):
    if num % mult == 0:
        print(num)