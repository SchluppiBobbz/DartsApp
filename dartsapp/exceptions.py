class OptionsNotSet(Exception):
    """ No Options were set"""


class NoPlayerRegistered(Exception):
    """ No Players were registered."""

class ValueDoesNotExist(Exception):
    """ The value does not exist on a dart-board """

class FieldDoesNotExist(Exception):
    """ The given field does not exist on a dart-board """
    
class BullseyeHasNoTriple(Exception):
    """ The bullseye does not have a triple-field. """