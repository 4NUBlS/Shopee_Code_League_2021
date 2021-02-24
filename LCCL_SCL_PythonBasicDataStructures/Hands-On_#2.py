from statistics import mean

numbers = []
above_avg = []
below_avg = []

while True:
    num = input('Enter a number (blank to quit): ')

    if num == '':
        break

    num = int(num)
    numbers.append(num)

if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    for num in numbers:
        if num < average:
            below_avg.append(num)
        elif num > average:
            above_avg.append(num)

print(f'Average: {average}')
print('Below average:', below_avg)
print('Above average:', above_avg)

average = mean(numbers)
print(average)