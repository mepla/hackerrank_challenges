
def word_order(words):
    distinct_words = []
    second_output = ''
    for word in words:
        if word not in distinct_words:
            distinct_words.append(word)
            second_output += str(words.count(word)) + ' '

    print len(distinct_words)
    print second_output.strip()

if __name__ == '__main__':
    TEST = True

    if TEST is True:
        lines = open('tests/input_10000').readlines()
    else:
        line_count = int(raw_input())
        lines = []
        for i in range(0, line_count):
            lines.append(raw_input())

    word_order(lines)
