from random import randint


def find_smallest_turns(snakes, ladders):
    def make_dice():
        return randint(1, 6)


    def helper(pos, turns):
        nonlocal smallest_turns
        if turns > 1000:
            return
        if pos > 100:
            return
        if pos == 100:
            if turns < smallest_turns:
                smallest_turns = turns
        i = pos + make_dice()
        if i in snakes:
            next_pos = snakes[i]
            helper(next_pos, turns + 1)
        elif i in ladders:
            next_pos = ladders[i]
            helper(next_pos, turns + 1)
        else:
            helper(i, turns + 1)


    smallest_turns = float('inf')
    helper(0, 0)
    print(smallest_turns)


if __name__ == '__main__':
    snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    find_smallest_turns(snakes, ladders)
