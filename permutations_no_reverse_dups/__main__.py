#!/usr/bin/python3.8

import itertools
import random

def with_repeats(colors, perm_length):
    used = []
    excluded = []

    for p in itertools.product(colors, repeat=perm_length):
        used.append(p)

    for p in itertools.product(colors, repeat=perm_length):
        # p[::-1] is how you reverse a tuple
        if p in used and p != p[::-1]:
            used.remove(p[::-1])
            excluded.append(p[::-1])

    return used, excluded


def no_repeats(colors, perm_length):
    used = []
    excluded = []

    for p in itertools.permutations(colors, perm_length):
        if p[0] < p[-1]:
            used.append(p)
        else:
            excluded.append(p)


def main():
    colors = ['red', 'yellow', 'green', 'blue', 'orange', 'purple']
    perm_length = 3

    allow_repeats = True
    shuffle = True

    used = []
    excluded = []

    if allow_repeats:
        used, excluded = with_repeats(colors, perm_length)
    else:
        used, excluded = no_repeats(colors, perm_length)

    if shuffle:
        random.shuffle(used)

    for p in excluded:
        print('Excluded {}'.format(p))

    for p in used:
        print(p)

    print('We may use {} of {} total permutations'.format(len(used), len(used) + len(excluded)))


if __name__ == '__main__':
    main()
