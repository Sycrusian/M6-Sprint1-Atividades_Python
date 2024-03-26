import math


def delta(a, b, c):
    return (b ** 2) - (4 * a * c)


def bhaskara(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        return "Delta Negativo"
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return (round(x1, 2), round(x2, 2))


print(bhaskara(7, 3, 4))
# Delta Negativo
print(bhaskara(1, 5, 2))
# x1=-0.44, x2=-4.56
print(bhaskara(3, 10, 2))
# x1=-0.21, x2=-3.12'
