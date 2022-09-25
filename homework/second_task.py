print('Write a program for. verification of the truth of the statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z for all values of the predicate')

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or z or y) == ((not x) and (not y) and (not z)):
                print(x, y, z)