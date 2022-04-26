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
        def test_save(self):
            """
             to test if credentials are saved in the password locker
            """
    
            self.new_user.save_user() #saving the new credentials
            self.assertEqual(len(User.user_list),1)
# third test case 
        def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
            
        def test_save_multiple_user(self):
            """
            test_save_multiple_user to save multiple user details
            """
            self.new_user.save_user()
            test_user = User("Grace","Graceeru","Gmail") # new contact
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

        

   
      

      


# delete user details test
# def test_delete_user(self):
#             '''
#             test_delete_user to test if we can remove a contact from our contact list
#             '''
#             self.new_user.save_user()
#             test_user = User("Test","user","0712345678","test@user.com") # new contact
#             test_user.save.user()

#             self.new_user.delete_user()# Deleting a contact object
#             self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()