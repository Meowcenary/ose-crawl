import unittest
from unittest import mock
from dice_roller import *

class TestDiceRoller(unittest.TestCase):
    def setUp(self):
        self.dr = DiceRoller()

    def test_roll(self):
        # randint_mock.return_value = 2
        # it should return a roll of 1d1 by default
        self.assertEqual(self.dr.roll(), 1)
        self.assertEqual(self.dr.roll(1), 1)

    def test_roll_multiple(self):
        # it should return a roll of 1d1 by default
        self.assertEqual(self.dr.roll_multiple(), 1)
        self.assertEqual(self.dr.roll_multiple(1), 1)
        self.assertEqual(self.dr.roll_multiple(1, 1), 1)

    @mock.patch('dice_roller.randint')
    def test_roll_die_string(self, randint_mock):
        randint_mock.return_value = 4
        self.assertEqual(self.dr.roll_die_string('1d4'), '4')
        self.assertEqual(self.dr.roll_die_string('4d4'), '16')

    @mock.patch('dice_roller.randint')
    def test_roll_string(self, randint_mock):
        randint_mock.return_value = 6

        # simple math
        self.assertEqual(self.dr.roll_string('10+20'), 30)
        self.assertEqual(self.dr.roll_string('10-10'), 0)
        self.assertEqual(self.dr.roll_string('10+20+30-30'), 30)
        self.assertEqual(self.dr.roll_string('100+1000'), 1100)

        # smaller dice
        self.assertEqual(self.dr.roll_string('1d6+6'), 12)
        self.assertEqual(self.dr.roll_string('2d6+6'), 18)
        self.assertEqual(self.dr.roll_string('2d8+6'), 18)

        # larger dice
        self.assertEqual(self.dr.roll_string('1d10+6'), 12)
        self.assertEqual(self.dr.roll_string('1d12+6'), 12)

        # different dice
        self.assertEqual(self.dr.roll_string('3d12+2d10+1d8'), 36)

        # wild
        self.assertEqual(self.dr.roll_string('3d12+2d10+1d8+2541-999'), 1578)

if __name__ == '__main__':
    unittest.main()
