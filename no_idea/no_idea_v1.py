
def no_idea(A, B, arr, n, m):
    happiness = 0
    for elem in arr:
        if elem in A:
            happiness += 1
        elif elem in B:
            happiness -= 1

    print happiness


if __name__ == '__main__':
    TEST = False

    if TEST is True:
        arr = range(0, 10000)
        A = set(range(0, 5000))
        B = set(range(5000, 10000))
        n = len(arr)
        m = len(A)

    else:
        first_inp = raw_input()
        second_inp = raw_input()
        third_inp = raw_input()
        fourth_inp = raw_input()

        n, m = first_inp.split(' ')
        arr = second_inp.split(' ')
        A = set(third_inp.split(' '))
        B = set(fourth_inp.split(' '))

    no_idea(A, B, arr, n, m)

# Passed 8/8