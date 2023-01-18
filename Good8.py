def sequence(n):
    if n == 0:
        return 1
    else:
        return sequence(n // 2) + sequence(n // 3)

for i in range(1, 11):
    print(sequence(i))