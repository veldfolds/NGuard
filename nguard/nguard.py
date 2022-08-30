
from .customexceptions import WrongTypeError


class Nguard():
    """A guard class to ensure the arguments in a constructor or method
       are valid"""

    def not_null(self, arg1):
        '''Ensures the input argument is not null'''
        if arg1 is None:
            raise Exception("{} should not be null".format(arg1))
        return self

    def greater_than(self, arg1, arg2):
        """Ensures the input argument is greater than a given threshold"""
        if arg1 <= arg2 :
            raise Exception("{} should be greater than {}".format(arg1, arg2))
        return self

    def less_than(self, arg1, arg2):
        """Ensures the input argument is less than a given threshold"""
        if arg1 >= arg2 :
            raise Exception("{} should be less than {}".format(arg1, arg2))
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
    
        