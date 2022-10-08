print("Set two numbers, you need to find the smallest common multiple")

from math import gcd

print("Enter two numbers")
a = int(input("a = "))
b = int(input("b = "))

def nok(fir, sec):
    return(fir*sec) // gcd(fir, sec)

print(nok(a, b))