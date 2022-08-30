from nguard.nguard import Nguard
from nguard.customexceptions import WrongTypeError
import unittest

class NguardTests(unittest.TestCase):

    nguard = Nguard()

    def test_inttype(self):
       with self.assertRaises(WrongTypeError):
                self.nguard.is_int("wonder")

    def test_stringtype(self):
        with self.assertRaises(WrongTypeError):
                self.nguard.is_string(8)

if __name__ == '__main__':
    unittest.main()