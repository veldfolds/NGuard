from customexceptions import WrongTypeError
import unittest
from guards import Nguard

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
