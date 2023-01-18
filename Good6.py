import math

def sum_series(n): # n это номер элемента
    if n == 0:
        return 1
    else:
        return (math.factorial(n) / (2 ** n)) + sum_series(n-1) # рекурсивно вызываем функцию


for i in range(1, 11): # выводим первые 10 элементов
    print(sum_series(i)) # вызываем функцию
