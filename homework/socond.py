print("Implement the RLE algorithm: implement a data compression and recovery module."
      "Input and output data are stored in separate text files")

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

s = input("Введите текст для кодировки: ")

with open("tamp.txt", "a", encoding="utf8") as output:
    output.write(coding(s))

print(f"Текст после кодировки: {coding(s)}")