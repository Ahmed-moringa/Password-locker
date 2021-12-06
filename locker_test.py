import unittest
from locker import User


class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('Ahmed','qwerty123')

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'Ahmed')
        self.assertEqual(self.new_user.password,'qwerty123')
