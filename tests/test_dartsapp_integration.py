#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `dartsapp` package."""


import unittest

from context import *



class TestDartsappIntegration(unittest.TestCase):
    """Tests for `dartsapp` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.player1 = player.Player("p1", "m")        
        self.game1 = game.x01()
        

    def test_register_player(self):
        self.game1.register_player(self.player1)

    def start_game(self):
        self.game1.register_player(self.player1)
        self.game1.set_options()
        self.game1.start()
    
    def test_start_game_501_with_options_and_players(self):   
        """ Test whether a 501 game was correctly started"""     
        self.start_game()
        self.assertEqual(self.game1.started, 1)
    
    def test_501_finished(self):
        """ Test whether a 501 game-status is finished at the end."""
        self.start_game()        
        self.play_perfect_game_501()
        self.assertEqual(self.game1.started, 0)

    def test_501_winner(self):
        """ Test if there is actually a winner """
        self.start_game()        
        self.play_perfect_game_501()
        self.assertEqual(self.game1.winner, self.player1)

    def play_perfect_game_501(self):
        """ play a perfect game """
        self.game1.throw_dart(20, 3)
        self.game1.throw_dart(20, 3)
        self.game1.throw_dart(20, 3)

        self.game1.throw_dart(20, 3)
        self.game1.throw_dart(20, 3)
        self.game1.throw_dart(20, 3)

        self.game1.throw_dart(20, 3)
        self.game1.throw_dart(19, 3)
        self.game1.throw_dart(12, 2)

    def test_start_game_without_options(self):
        """ What happens, when options aren't set """
        self.game1.register_player(self.player1)
        with self.assertRaises(OptionsNotSet):
            self.game1.start()

    def test_start_game_without_players(self):
        """ What happens, when no players are registered """
        with self.assertRaises(NoPlayerRegistered):
            self.game1.start()

    def tearDown(self):
        """Tear down test fixtures, if any."""
        self.game1 = None
        self.player1 = None

    def test_000_something(self):
        """Test something."""

if __name__ == "__main__":
    unittest.main(buffer=True) 

