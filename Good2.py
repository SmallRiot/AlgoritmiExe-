from tkinter import Tk, Canvas
import time

# Объявляем главные переменные
iterations = 7 # Количество итераций фрактала
window_title = "Cantor Set" # Заголовок окна
width_max = 1200 # Максимальная ширина окна
height_max = width_max * (2/5) # Максимальная высота окна
x_start = 10 # Начальная координата x
y_start = 20 # Начальная координата y
y_step = 60 # Шаг по вертикали между линиями
color_bkg = "blue" # Цвет фона
color_line = "white" # Цвет линии
width_line = 5 # Ширина линии
delay = 0.2 # Задержка между отрисовкой линий

# Функция рисования линии
def draw_line(x1, x2, y):
    canvas.create_line(x1, y, x2, y, fill=color_line, width=width_line)
    canvas.update()  # Отрисовывает линии пошагово

# Рекурсивная функция для рисования фрактала
def cantor(x1, x2, y, iteration):
    if iteration > 0:
        time.sleep(delay)
        draw_line(x1, x2, y) # Рисуем линию
        point1 = x1 + (x2-x1) * (1/3) # Рассчитываем координаты для точки 1
        point2 = x1 + (x2-x1) * (2/3) # Рассчитываем координаты для точки 2
        y2 = y + y_step # Рассчитываем новую координату y
        cantor(x1, point1, y2, iteration-1) # Рекурсивно вызываем функцию с новыми координатами для левой части
        cantor(point2, x2, y2, iteration-1) # Рекурсивно вызываем функцию с новыми координатами для правой части


# Главная функция
if __name__ == "__main__":
    # Создаем главное окно
    window = Tk()
    window.title(window_title)

    # Создаем холст
    canvas = Canvas(window, width=width_max, height=height_max, background=color_bkg)
    canvas.grid()

    # Вызываем рекурсивную функцию и отображаем холст
    cantor(x_start, width_max - x_start, y_start, iterations)

    # Запускаем главное окно
    canvas.mainloop()
