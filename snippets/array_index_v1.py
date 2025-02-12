def index(arr, value, size):
    for i in range(size):
        if arr[i] == value:
            return i
    return -1

fib8 = [0, 1, 1, 2, 3, 5, 8, 13]

s = index(fib8, 3, 8)

print(s)