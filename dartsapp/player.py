# -*- coding: utf-8 -*-
"""Player module."""

class Player(object):
    
    ARROWS_LEFT = 0
    GAMES_PLAYED = 0
    GAMES_WON = 0
    GAME_HISTORY = {}
    RECENT_FIELDS = []
    ACTUAL_HAND = []
    
    
    def __init__(self, name="player", gender="m"):
        if name:
            self.name = name
        self.gender = gender
    
    def check_hand(self):
        if self.ARROWS_LEFT > 0:
            return 1
        else:
            return 0
    
    def new_darts(self, number_of_arrows=3):
        self.ARROWS_LEFT = number_of_arrows
        self.ACTUAL_HAND = []
        
    def finish_hand(self):
        self.ACTUAL_HAND = []
        self.ARROWS_LEFT = 0    
    
    def throw_dart(self, throw):
        if self.ARROWS_LEFT > 0:
            self.actual_field = throw
            self.RECENT_FIELDS.append(throw)
            self.ARROWS_LEFT -= 1   
            self.ACTUAL_HAND.append(throw.points)            
        else:
            raise Exception("No Darts left in actual hand.")
        
    
    def _play_game(self):
        self.RECENT_FIELDS = []
        self.GAMES_PLAYED += 1
    
    def _win_game(self, game):
        self.GAMES_WON += 1
        timestamp = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S")
        self.GAME_HISTORY[timestamp] = game
        
    
    def register_player(self):
        pass
    
    def rename_player(self, new_name):
        self.name = new_name
