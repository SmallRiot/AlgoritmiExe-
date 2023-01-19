import math

def min_max_distance(coords, n):
    # Если количество точек меньше или равно 1, то возвращаем минимум и максимум как бесконечность
    if n <= 1:
        return (float('inf'), -1, -1), (float('inf'), -1, -1)

    # Инициализируем минимальное и максимальное расстояние как бесконечность и -1 соответственно
    min_dist, max_dist = float('inf'), -1
    # Инициализируем минимальную и максимальную пару точек как (-1, -1)
    min_pair, max_pair = (-1, -1), (-1, -1)

    # Перебираем все пары точек
    for i in range(n):
        for j in range(i+1, n):
            # Вычисляем расстояние между точками
            dist = math.sqrt((coords[2*i] - coords[2*j])**2 + (coords[2*i + 1] - coords[2*j + 1])**2)
            # Если расстояние меньше текущего минимума, то обновляем минимум
            if dist < min_dist:
                min_dist = dist
                min_pair = (i, j)
            # Если расстояние больше текущего максимума, то обновляем максимум
            if dist > max_dist:
                max_dist = dist
                max_pair = (i, j)

    # Возвращаем минимум и максимум в виде кортежей (расстояние, номер первой точки, номер второй точки)


    return (min_dist, min_pair[0], min_pair[1]), (max_dist, max_pair[0], max_pair[1])


coords = [0, 0, 3, 4, 1, 1, 5, 6, 9, 9]
min_dist, max_dist = min_max_distance(coords, len(coords)//2)
print("Minimum distance:", min_dist[0], "between points", min_dist[1], "and", min_dist[2])
print("Maximum distance:", max_dist[0], "between points", max_dist[1], "and", max_dist[2])


