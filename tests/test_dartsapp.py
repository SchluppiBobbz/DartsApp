#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `dartsapp` package."""


import unittest

from context import game, darts_helper, player



class TestDartsapp(unittest.TestCase):
    """Tests for `dartsapp` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def integration_test(self):
        player1 = player.Player("p1", "m")
        
        game1 = game.x01()
        game1.set_options()
        game1.register_player(player1)

        game1.start()
