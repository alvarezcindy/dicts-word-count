import sys


def count_words(filename):

    word_count = {}

    with open(filename) as text:
        for line in text:
            words = line.split()
            for word in words:
                if word[-1] in "_.,?!;:\'\"":
                    word = word[:-1]
                word_count[word.lower()] = word_count.get(word, 0) + 1

    for word, number in word_count.items():
        print("{} {}".format(word, number))


count_words(sys.argv[1])
