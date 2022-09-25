print('Find the maximum number of 5')
max_val = 0;

print('Enter numbers')
for i in range(5):
    a = int(input())
    if a > max_val:
        max_val = a

print(max_val)