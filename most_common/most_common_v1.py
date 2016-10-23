from collections import Counter


def most_common(string):
    c = Counter(string).most_common(3)
    sorted(c, key=lambda x: x[0])
    for i in c:
        print '{} {}'.format(i[0], i[1])

if __name__ == '__main__':
    string = raw_input()
    most_common(string)
