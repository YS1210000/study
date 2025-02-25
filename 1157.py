word = input().upper()
word_set = list(set(word))
count_word = []

for i in word_set:
    count_word.append(word.count(i))

if count_word.count(max(count_word)) > 1:
    print("?")
else:
    print(word_set[count_word.index(max(count_word))])
