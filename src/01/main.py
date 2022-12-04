#!/usr/bin/env python3
import unittest


def getlines():
    with open('data/input.txt') as f:
        lines = f.readlines()

        return lines


def findmax(lines):
    amts = []
    amt = 0

    for line in lines:
        if line == "\n":
            amts.append(amt)
            amt = 0
        else:
            amt += int(line)

    amts.append(amt)

    return max(amts)


class MaxCalorieInventoryTest(unittest.TestCase):
    def test_findmax(self):
        lines = ['1', '2', '\n', '1', '\n', '5', '6']
        highest = findmax(lines)

        self.assertEqual(highest, 11)


    def test_findmax_bigger_data(self):
        lines = getlines()
        highest = findmax(lines)

        self.assertEqual(highest, 69836)


if __name__ == '__main__':
    unittest.main()


