from math import sqrt
 
# Функция для подсчёта дистанции
# между двумя точками
def dist(p1x, p1y, p2x, p2y):
     
    x0 = p1x - p2x
    y0 = p1y - p2y
    return x0 * x0 + y0 * y0
 
# Функция для подсчёта максимума и минимума
# расстояния между двумя точками
def maxDist(p):
 
    n = len(p)
    maxm = 0
    minm = 100
    # Перебор всех возможных пар
    for i in range(n):
        if i % 2 == 0:
            for j in range(i+2, n):
                if j % 2 == 0:
                    # Обновление наибольшего и наименьшего расстояний
                    maxm = max(maxm, dist(p[i],p[i+1], p[j], p[j+1]))
                    minm = min(minm, dist(p[i],p[i+1], p[j], p[j+1]))
 
    # Вывод максимального и минимального рассстояний
    return (sqrt(maxm), sqrt(minm))
     
if __name__ == '__main__':
     
    # Количество ячеек массива
    n = 10
 
    p = (4, 0, 0, 2, -1, -7, 1, 10, 2, -3)
     
    # Данные точки ( можно удалить)
   # p.append([4, 0])
   # p.append([0, 2])
   # p.append([-1, -7])
   # p.append([1, 10])
   # p.append([2, -3])
 
    # Вызор функции по поиску
    print(maxDist(p))