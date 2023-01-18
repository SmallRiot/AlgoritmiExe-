import turtle

# Определяем начальное условие и правила для L-системы
axiom = "F"
newf = {"F":"F+F-F-F-F+F+F+F-F"}
iterations = 3 # Количество итераций
alpha = 45 # угол начального направления
angle = 90 # угол поворота

# функция создания L-системы
def create_l_system(iters, axiom, newf): 
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(newf[i] if i in newf else i for i in start_string)
        start_string = end_string
    return end_string

# функция отрисовки L-системы
def draw_l_system(t, instructions, angle, distance):
    for liter in instructions:
        if liter == 'F':
            t.forward(distance) # движение вперед
        elif liter == '+':
            t.right(angle) # поворот направо
        elif liter == '-':
            t.left(angle) # поворот налево

# функция запуска программы
def create(iterations, axiom, rules, angle, length=20, size=2, width=800, height=800):
    inst = create_l_system(iterations, axiom, newf)
    t = turtle.Turtle() # создаем экземпляр черепашки
    wn = turtle.Screen() # создаем экран
    wn.setup(width, height) # задаем размеры экрана
    t.up() # поднимаем черепашку
    t.left(alpha) # поворачиваем в начальное направление
    t.down() # опускаем черепашку
    t.speed(10) # устанавливаем скорость
    t.pensize(size) # размер линии
    draw_l_system(t, inst, angle, length) # вызываем функцию отрисовки
    t.hideturtle() # скрываем черепашку
    wn.exitonclick() # закрываем окно по клику

create(iterations, axiom, newf, angle)

