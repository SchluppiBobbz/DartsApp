# -*- coding: utf-8 -*-
"""Main module."""
import time
import datetime
from collections import defaultdict, namedtuple

class DartGame(object):
    players = None
    actual_player = None
    
    def __init__(self):
        self.round = 0
        self.players = []
    
    def register_player(self, player):
        if player.name not in self.players:
            self.players.append(player)
    
    def set_options(self, config):
        pass
    
    def start(self):
        pass



# x01-Type like 301, 501, 701        
class x01(DartGame):
    finish_options = {
        1: "straight_out",
        2: "double_out",
        3: "triple_out"
    }
    
    openinig_options = {
        1: "straight_in",
        2: "double_in",
        3: "triple_in"
    }
    number_of_darts = 3
    
    def __init__(self):
        super().__init__()
        self.started = 0
        self.initialized = 0
    
    def set_options(self, variation=5, finish_type=2, opening_type=1):
        assert isinstance(variation, int), "Integer required."
        self.target_points = int("%s01" % variation)    
        self.initialized = 1
        self.finish_type =  finish_type
        self.opening_type = opening_type
        
    def start(self):
        if self.players and self.initialized:
            # Set All Points to 0
            for player in self.players:
                player.scoreboard = self.target_points
                player._play_game()
            self.started = 1
            self.rounds = 0
            self.player_counter = 0
            self.next_player()
        else:
            if not self.initialized:
                print ("ERROR: Game-Options not set.")
            if not self.players:
                print ("ERROR: No Players are registered.")
    
    def next_player(self):
        if not self.started:
            print ("You have to start the game first.")
            return
        
        # Set new round in case player 1 is on turn
        if self.player_counter % len(self.players) == 0:
            self.rounds += 1
        act_no = self.player_counter % len(self.players)
        self.actual_player = self.players[act_no]
        self.player_counter += 1
        print ("\nPlayer %s is now on turn!" % self.actual_player.name)
        print  ("%s points to finish." % self.actual_player.scoreboard)
        # Give actual player new darts        
        self.actual_player.new_darts(self.number_of_darts)
        
    
    def throw_dart(self, throw):
            
        self.actual_player.throw_dart(throw)
        
        # TODO: Double/Trible in
        if self.actual_player.scoreboard - throw.points >= self.finish_type:
            self.actual_player.scoreboard -=  throw.points
            
        elif (self.actual_player.scoreboard - throw.points == 0) and (
              self.finish_type == 1 or throw.field_type == self.finish_type):
            self.actual_player.scoreboard = 0
            self.finish_game()

        else:
            print ("Busted - Too much points.")
            self.reset_score()
        
        if not self.actual_player.check_hand() and self.started:
            self.print_score()
            self.next_player()
        
    
    def finish_game(self):
        self.actual_player.finish_hand()        
        print ("%s won the game within %s rounds." % (self.actual_player.name, self.rounds))
        self.winner = self.actual_player
        self.actual_player._win_game(self)
        self.started = 0
    
    def print_score(self):      
        print ("%s requires %s points to finish." % (self.actual_player.name, self.actual_player.scoreboard))
    
    def reset_score(self):
        for points in self.actual_player.ACTUAL_HAND[:-1]:
            self.actual_player.scoreboard += points
        self.actual_player.finish_hand()

    def __str__(self):
        print ("Registered Players: %s" % ",".join([p.name for p in self.players]))
        print ("x01-variation (points to finish): %s" % self.target_points)
        for player in self.players:
            print ("%s requires %s points to finish." % (player.name, player.scoreboard))
        return ""