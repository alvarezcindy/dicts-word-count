import sys
from collections import Counter


def count_words(filename):

    with open(filename) as text:
        words = text.read().split()

        for i in range(len(words)):
            words[i] = words[i].lower()
            if words[i][-1] in "_.,?!;:\'\"":
                words[i] = words[i][:-1]

        word_count = Counter(words)

    for word, number in word_count.items():
        print("{} {}".format(word, number))


count_words(sys.argv[1])
