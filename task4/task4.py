import sys


numbers_path = sys.argv[1]

with open(numbers_path, encoding="utf-8-sig") as numbers_file:
    numbers = list(map(int, numbers_file.read().split()))

numbers.sort()
target = numbers[len(numbers) // 2]

moves = 0
for number in numbers:
    moves += abs(number - target)

if moves <= 20:
    print(moves)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
