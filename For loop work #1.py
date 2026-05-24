colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)
for number in range(1,5):
    print(number)
# in a real world situation the singular loop variable helps to keep it from being confusing
# because a loop looks at 1 variable at a time till the end of the list
numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total = total + number
    print(total)
# because print is inside the for loop it prints everytime the loop runs
# to print just the total of numbers put print outside of the for loop
# like this:
numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total = total + number
print(total)

for number in range(1,11):
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')

