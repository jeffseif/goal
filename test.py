#! /usr/bin/env python3

# Import

import goal
import unittest

# Classes

class TestGoal(unittest.TestCase):

    def test_goal(self):
        expected = 'goal'
        output = goal.g()('al')

        self.assertEqual(output, expected)

    def test_gooal(self):
        expected = 'gooal'
        output = goal.g()()('al')

        self.assertEqual(output, expected)

    def test_goooal(self):
        expected = 'goooal'
        output = goal.g()()()('al')

        self.assertEqual(output, expected)

    def test_gooooal(self):
        expected = 'gooooal'
        output = goal.g()()()()('al')

        self.assertEqual(output, expected)

    def test_goooooal(self):
        expected = 'goooooal'
        output = goal.g()()()()()('al')

        self.assertEqual(output, expected)

    def test_gooooooal(self):
        expected = 'gooooooal'
        output = goal.g()()()()()()('al')

        self.assertEqual(output, expected)

    def test_goooooooal(self):
        expected = 'goooooooal'
        output = goal.g()()()()()()()('al')

        self.assertEqual(output, expected)

# Script

if __name__ == '__main__':
    unittest.main()
