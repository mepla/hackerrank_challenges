from collections import Counter


def most_common(string):
    c = Counter(string).most_common(3)
    char_to_num = {}
    num_to_char = {}
    for i in c:
        char_to_num[i[0]] = i[1]
        if i[1] not in num_to_char:
            num_to_char[i[1]] = []

        num_to_char[i[1]].append(i[0])

    all_keys = sorted(num_to_char.keys(), reverse=True)
    for i in all_keys:
        for j in sorted(num_to_char[i]):
            print '{} {}'.format(j, i)

if __name__ == '__main__':
    string = raw_input()
    most_common(string)

# Passed 8/8
