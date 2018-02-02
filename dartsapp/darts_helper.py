# -*- coding: utf-8 -*-
"""COllection of Dart-helpers"""
from dartsapp.exceptions import BullseyeHasNoTriple, ValueDoesNotExist, FieldDoesNotExist

class Throw(object):
    """This class is all about the Throw:
    - which field-type was hit (single, double, triple)
    - how many points were gained
    """

    AVAILABLE_VALUES = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25]
    AVAILABLE_FIELDS = {1: "Single",
                        2: "Double", 
                        3: "Triple"}
    
    def __init__(self, value, field_type=1):
        """A dart was thrown
        
        Arguments:
            value {int} -- how much points were one the field hit
        
        Keyword Arguments:
            field_type {value-list} -- what field-type was hit (default: {1})
        
        Raises:
            AttributeError -- Bull has only Single or Double, no Triple
        """
        if  value not in self.AVAILABLE_VALUES:
            raise ValueDoesNotExist()
        self.value = value
        

        if field_type not in self.AVAILABLE_FIELDS.keys():
            raise FieldDoesNotExist()
        self.field_type = field_type
        
        if self.value == 25 and self.field_type == 3:
            raise BullseyeHasNoTriple("A triple-Bull does not exist.")
        else:
            self.points = self.value * self.field_type
    
    
    def __repr__(self):
        return str("Field: %s, Segment: %s" %(self.value, self.AVAILABLE_FIELDS[self.field_type]))
    
    
    
    
    