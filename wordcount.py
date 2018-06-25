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

    for word, number in sorted(word_count.items(), key=lambda pair: (-pair[1], pair[0])):
        print("{} {}".format(word, number))

    # items = list(word_count.items())
    # items.sort()
    # items.sort(key=lambda pair: pair[1], reverse=True)


count_words(sys.argv[1])
