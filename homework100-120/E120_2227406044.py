with open('article.txt', 'r') as f:
    text = f.read()
words = list(set(text.split()))
length_count = {}
for word in words:
    length = len(word)
    if length in length_count:
        length_count[length] += 1
    else:
        length_count[length] = 1
words.sort(key=len)
with open('new_article_classify.txt', 'w') as f:
    for length, count in length_count.items():
        length_words = words[:count]
        f.write(f"{length}:{count},{' '.join(length_words)}\n")
        words = words[count:]