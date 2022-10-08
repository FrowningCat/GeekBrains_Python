print("Find the roots of the quadratic equation using the module. Request the values of A B C, and write them to a file")

from math import sqrt

print("Enter the coefficients of the quadratic equation")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b ** 2 - 4 * a * c
sqrtd = sqrt(d)

with open("tamp.txt", "a", encoding="utf8") as output:
    output.write(f"The equation: {a}*x^2 + {b}*x + {c}\n")
    if d > 0 and a:
        x1 = (-b + sqrtd) / (2 * a)
        x2 = (-b + sqrtd) / (2 * a)
        output.write(f"Roots= {x1, x2}\n")
    elif d == 0:
        x = -b / (2 * a)
        output.write(f"Root = {x}\n")
    else:
        output.write("There are no roots")
