n = int(input())

array = list(map(int, input().split()))

for i in range(n // 2):
    array[i], array[n - 1 - i] = array[n - 1 - i], array[i]

for i in range(0, n):
    print(array[i], end = " ")