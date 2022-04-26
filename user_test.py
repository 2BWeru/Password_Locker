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

 # second testcase
    # a test to save User objects
        def test_save(self):
          """
        to test if credentials are saved in the password locker
        """
          self.new_user.save_user() #saving the new credentials
          self.assertEqual(len(User.user_list),1)

           # second testcase
    # a test to save User objects
        def tearDown(self):
              '''
            tearDown method that does clean up after each test case has run.
            '''
        User.user_list = []

if __name__ == '__main__':
    unittest.main()