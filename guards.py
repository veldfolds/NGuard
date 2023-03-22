# Importing the custom exceptions
from .customexceptions import WrongTypeError, InEqualityError, EqualityError

class Nguard():
    """A guard class to ensure the arguments in a constructor or method
       are valid"""
    
    def not_null(self, *args):
        '''Ensures the input arguments are not null'''
        for arg in args:
            if arg is None:
                raise WrongTypeError("{} should not be null".format(arg))

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

        if not isinstance(x, y):
            raise WrongTypeError("{} is not {} type".format(x, y.__name__))

    def is_equal(self, x, y):
        '''
            Check if two arguments are equal
            If equal return True, else raise EqualityError
        '''
        if (x != y):
            raise EqualityError("{} is not equal to {}".format(x, y))
        else:
            return True

