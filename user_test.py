import unittest
from user import User

class TestUser(unittest.TestCase):
        '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
        def setUp(self):
             self.new_user = User("bettyweru" , "b345" , "Todolist") # create contact object

        def test_start(self):
                self.assertEqual(self.new_user.user_name,"bettyweru")
                self.assertEqual(self.new_user.pass_word,"b345")
                self.assertEqual(self.new_user.app_name,"Todolist")

if __name__ == '__main__':
    unittest.main()