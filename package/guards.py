
import unittest
from customexceptions import WrongTypeError, InEqualityError, EqualityError

class Nguard():
    """A guard class to ensure the arguments in a constructor or method
       are valid"""
    
    def not_null(self, arg1):
        '''Ensures the input argument is not null'''
        if arg1 is None:
            raise WrongTypeError("{} should not be null".format(arg1))
        return self

    def greater_than(self, arg1, arg2):
        """Ensures that arg1 is greater than arg2"""
        if arg1 <= arg2 :
            raise InEqualityError("{} should be greater than {}".format(arg1, arg2))
        return self

    def less_than(self, arg1, arg2):
        """Ensures the arg1 is less arg2"""
        if arg1 >= arg2 :
            raise InEqualityError("{} should be less than {}".format(arg1, arg2))
        return self

    def is_int(self, arg):
        """Ensures the input argument is type int"""
        self.is_type(arg, int)
        return self

    def is_string(self, arg):
        """Ensures the input argument is type string"""
        self.is_type(arg, str)
        return self

    def is_float(self, arg):
        """Ensures the input argument is type float"""
        self.is_type(arg, float)
        return self

    def is_list(self, arg):
        """Ensures the input argument is type list"""

        self.is_type(arg, list)
        return self
        
    def is_dictionary(self, arg):
        """Ensures the input argument is type dictionary"""
        self.is_type(arg, dict)
        return self

    def is_type(self, x, y):
        """To avoid repetitions i have wrapped the type checks methods
        within this helper function"""
        if type(x) != y:
            raise WrongTypeError("{} is not {} type".format(x, y))
    
        
class Entity():
    '''Sample case study'''
    def __init__(self, name, id, rank) -> None:
        (Nguard().is_string(name)
                 .is_int(id)
                 .is_int(rank)
        )

        self.name = name
        self.id = id 
        self.rank = rank


class NguardTests(unittest.TestCase):

    nguard = Nguard()

    def test_inttype(self):
       with self.assertRaises(WrongTypeError):
                self.nguard.is_int("wonder")

    def test_stringtype(self):
        with self.assertRaises(WrongTypeError):
                self.nguard.is_string(8)

    def test_subject(self):
        with self.assertRaises(WrongTypeError):
                Entity("object", "objectid", 4)




unittest.main()