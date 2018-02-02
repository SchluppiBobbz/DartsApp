#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `dartsapp` package."""


import unittest

from context import darts_helper
from context import ValueDoesNotExist, FieldDoesNotExist,\
                                BullseyeHasNoTriple



class TestThrow(unittest.TestCase):
    """Tests for `dartsapp` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        # self.throw = darts_helper.Throw()

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_points(self):
        """ Test if sum of points is correctly calculated. """
        throw = darts_helper.Throw(20,2)
        self.assertEqual(throw.points, 40)

    def test_wrong_value(self):
        """Test what happens if a value is not supported."""
        with self.assertRaises(ValueDoesNotExist):
            darts_helper.Throw(26,1)

    def test_wrong_fieldtype(self):
        """Test what happens if a type was selected, which does not exist"""
        with self.assertRaises(FieldDoesNotExist):
            darts_helper.Throw(20,5)

    def test_wrong_bull(self):
        """Test a triple-bull, which really should not exist!"""
        with self.assertRaises(BullseyeHasNoTriple):
            darts_helper.Throw(25,3)

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestThrow)
    unittest.TextTestRunner(verbosity=2).run(suite)