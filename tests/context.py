import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dartsapp import game, player, darts_helper
from dartsapp.exceptions import BullseyeHasNoTriple, FieldDoesNotExist,\
                                NoPlayerRegistered, OptionsNotSet,\
                                ValueDoesNotExist