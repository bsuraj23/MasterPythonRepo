def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

sentence = "Python is fun and Python is easy"
print(word_frequency(sentence))

#TODO

#variable length args