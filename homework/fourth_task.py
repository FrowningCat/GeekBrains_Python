print("The natural degree k is given. Randomly generate a list of coefficients (from 0 to 10) of the polynomial,"
      " write the resulting polynomial to the file at least 3 times")

from random import choice

def polynom(num: int):
      if num < 1:
            return 0

      poly = ""
      num_list = range(0, 10)

      with open("poly.txt", "a", encoding="utf-8") as my_f:
            for i in range(num, 0, -1):
                  value = choice(num_list)
                  if value:
                        poly += f"{value}*x^{i} {choice('+-')}"

            my_f.write(f"{poly}{choice(num_list)} = 0 \n")

for _ in range(3):
      polynom(int(input("Enter the numbers: ")))