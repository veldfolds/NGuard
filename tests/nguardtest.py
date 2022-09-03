import unittest
from nguard.customexceptions import WrongTypeError, EqualityError, InEqualityError
from nguard.nguard import Nguard


class TestEntity():
    '''Sample case study to be used in the tests'''
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
                TestEntity("object", "objectid", 4)




unittest.main()