import math
 
a = 0.0; b = 1.0; e = 0.0001
def f(x):
    return x**4 - 3*x**3 - 6*x**2 + 2
y1 = f(a); y2 = f(b)
if y1 * y2 >= 0:
    print ("Корней нет")
else:
    n = 1
    x = (a+b)/2
    y3 = f(x)
    while (abs(y3) > e):
        x = (a+b)/2
        y3 = f(x);
        if y1 * y3 < 0:
            b = x
        else:
            a = x
            n += 1
    print ("x = %15.10f" % (x))