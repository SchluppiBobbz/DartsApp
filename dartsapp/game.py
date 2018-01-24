# -*- coding: utf-8 -*- """Main module.""" import time import datetime from collections import defaultdict, namedtuple 


class DartGame(object):
    """
    Main DartGame Class
    """
    players = None
    actual_player = None
    def __init__(self):
        """Start game
        """

        self.round = 0
        self.players = []
    
    def register_player(self, player):
        """Register player in given game
        
        Arguments:
            player {dartsapp.Player} -- Instance of Player which shall be
            registered
        """

        
        if player.name not in self.players:
            self.players.append(player)
    
    def set_options(self, config):
        pass
    
    def start(self):
        pass



# x01-Type like 301, 501, 701        
class x01(DartGame):
    """The most popular game-type of darts: x01

    the main objective is, to reduce the score from x01 (e.g. 501) to 0.
    The first plyer who hits exactly 0 wins. Most of the time the final
    dart must hit a double field to win the game (double out).

    """

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
        """Set options of x01
        
        Keyword Arguments:
            variation {integer} -- the digit(s) which stand for the 'x'.
                This defines the overall points a player has to reduce in order
                to win. (default: {5})
            finish_type {Integer:[1,2,3]} -- Set the type of field which
                must be hit with the final dart to win the game:
                1: straight out
                2: double out
                3: triple out
                (default: {2})
            opening_type {Integer:[1,2,3]} -- Sets the type of field which
                must be hit with a dart in order to begin the game:
                1: straight in
                2: double in
                3: triple in
                (default: {1})"""

        assert isinstance(variation, int), "Integer required."
        self.target_points = int("%s01" % variation)    
        self.initialized = 1
        self.finish_type =  finish_type
        self.opening_type = opening_type
        
    def start(self):
        """Start the game
        """

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
        """Go on to the next player
        """

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
        """Throw your dart
        
        Arguments:
            throw {dartsapp.throw.Throw} -- A throw is an object created via
                the dartsapp.throw.Throw class

        """

            
        self.actual_player.throw_dart(throw)
        
        # TODO: Double/Trible in
        if self.actual_player.scoreboard - throw.points >= self.finish_type:
            self.actual_player.scoreboard -=  throw.points
            
        elif (self.actual_player.scoreboard - throw.points == 0) and (
              self.finish_type == 1 or throw.field_type == self.finish_type):
            self.actual_player.scoreboard = 0
            self._finish_game()

        else:
            print ("Busted - Too much points.")
            self.reset_score()
        
        if not self.actual_player.check_hand() and self.started:
            self.print_score()
            self.next_player()
        
    
    def _finish_game(self):
        """FOR INTERNAL USE ONLY.
        This finishs the game. 
        """

        self.actual_player.finish_hand()        
        print ("%s won the game within %s rounds." % (self.actual_player.name, self.rounds))
        self.winner = self.actual_player
        self.actual_player._win_game(self)
        self.started = 0
    
    def print_score(self):
        """Print the actual score to the commandline
        """

        print ("%s requires %s points to finish." % (self.actual_player.name, self.actual_player.scoreboard))
    
    def reset_score(self):
        """Resets the score, in case a player has busted.
        """

        for points in self.actual_player.ACTUAL_HAND[:-1]:
            self.actual_player.scoreboard += points
        self.actual_player.finish_hand()

    def __str__(self):
        print ("Registered Players: %s" % ",".join([p.name for p in self.players]))
        print ("x01-variation (points to finish): %s" % self.target_points)
        for player in self.players:
            print ("%s requires %s points to finish." % (player.name, player.scoreboard))
        return ""