import sys


def circular_path(size, interval_length):
    position = 0
    jumps = interval_length - 1
    starts = []

    while True:
        starts.append(str(position + 1))

        position = (position + jumps) % size

        if position == 0:
            break

    return "".join(starts)


n1, m1, n2, m2 = map(int, sys.argv[1:])
first_path = circular_path(n1, m1)
second_path = circular_path(n2, m2)
print(first_path + second_path)
