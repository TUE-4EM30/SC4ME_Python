def index(arr, value):
    for i, v in enumerate(arr):
        if v == value:
            return i
    return -1

fib8 = [0, 1, 1, 2, 3, 5, 8, 13]

s = index(fib8, 3)

print(s)