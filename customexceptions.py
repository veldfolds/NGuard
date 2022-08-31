
class WrongTypeError(Exception):
    '''Raised when input type doesn't match the expected type'''
    pass

class EqualityError(Exception):
    '''Raised when input value is not equal to expected value'''
    pass

class InEqualityError(Exception):
    '''Raised when either input value is not less than a predetermined value or
    input value is not greater than a predetermined value '''
    pass