print('Create a list of arbitrary words, determine the index of the second input')

from random import choices

def form_words_list(count, source):
    result = []
    for i in range(count):
        temp = choices(source, k = 3)
        result.append("".join(temp))
    return result

def find_sec_enc(word, word_list):
    if word_list.count(word) > 1:
        first_encounter = word_list.index(word)
        print(f"Second occurrence: {word_list.index(word, first_encounter + 1)}")
    else:
        print("-1")

count, source = int(input()), input()

words = form_words_list(count, source)
print(words)

find_sec_enc(input(), words)
