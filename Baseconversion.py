#! /usr/bin/env python3

import sys
import string

digs = string.digits + string.ascii_letters


def int2base(number: int, base: int) -> str:
    if number < 0:
        sign = -1
    elif number == 0:
        return digs[0]
    else:
        sign = 1
    number *= sign
    digits = []
    while number:
        digits.append(digs[number % base])
        number //= base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)


def convert(base_from: int, base_to: int, number: str) -> str:
    number = int(number, base_from)
    return int2base(number, base_to)


if __name__ == '__main__':
    try:
        base_to = sys.argv[sys.argv.index('to') + 1]
    except ValueError:
        base_to = 10
    try:
        base_from = sys.argv[sys.argv.index('from') + 1]
    except ValueError:
        base_from = 10
    try:
        base_from = int(base_from)
        base_to = int(base_to)
    except ValueError:
        print("You have not entered valid bases")
        sys.exit(1)
    converted = convert(base_from, base_to, sys.argv[1])
    print(converted)
