def count_words(filename):

    word_count = {}

    with open(filename) as text:
        for line in text:
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

    for word, number in word_count.items():
        print("{} {}".format(word, number))


count_words("test.txt")
# count_words("twain.txt")
