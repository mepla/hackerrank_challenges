from collections import OrderedDict


def word_order(words):
    all_dict = OrderedDict()
    for word in words:
        if word not in all_dict:
            all_dict[word] = '1'
        else:
            all_dict[word] = str(int(all_dict[word]) + 1)

    print len(all_dict)
    print ' '.join(all_dict.values())

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

# Passed 8/8
