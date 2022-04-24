import string
import random
import unittest
from account import User

class Testuser(unittest.TestCase):
    '''
    This test class defines test cases for the User class behaviour

    Args:
        unittest.TestCase: TestCase class that helps create test cases
    '''

    def SetUp(self):
        self.new_account = User("Morces", "Emkay33")

    def test_init(self):
        self.assertEqual(self.new_account.username, "Morces")
        self.assertEqual(self.new_account.password, "emkay33")

    def test_save_user(self):
        self.save_user()
        self.assertEqual(len(User.user_list),1)
    def test_delete_user(self):
        self.delete()
        self.assertEqual(len(User.user_list),0)

    if __name__ == '__main__' :
        unittest.main()


    