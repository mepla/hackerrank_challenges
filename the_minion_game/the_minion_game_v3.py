import time


def start_minion_game(game_string):
    vowels = ['A', 'O', 'U', 'E', 'I']
    stuart_points = 0
    kevin_points = 0
    length = len(game_string)
    # total_start = time.time()
    for i, ch in enumerate(game_string):
        # start = time.time()
        # print 'inner loop started for {}'.format(i)
        if ch in vowels:
            kevin_points += length - i
        else:
            stuart_points += length - i
        # print 'inner loop started for {}, took: {}'.format(i, str(time.time() - start))

    # print 'Total took: {}'.format(str(time.time() - total_start))

    if stuart_points == kevin_points:
        print 'Draw'
    elif stuart_points > kevin_points:
        print 'Stuart {}'.format(stuart_points)
    else:
        print 'Kevin {}'.format(kevin_points)


if __name__ == '__main__':
    string = raw_input()
    if not string.isalpha():
        print 'Please enter an uppercase string'
    string = string.upper()
    start_minion_game(string)

# Passed 15/15 :D
