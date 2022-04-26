
import unittest
from user import User
import pyperclip

class TestUser(unittest.TestCase):
        '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
        
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
        def test_delete_user(self):
              '''
               test_delete_user to test if we can remove a contact from our contact list
              '''
              self.new_user.save_user()
              test_user = User("Grace","Graceeru","Gmail") # new contact
              test_user.save_user()

              self.new_user.delete_user()# Deleting a contact object
              self.assertEqual(len(User.user_list),1)
     
    #  to find app name

        def test_find_user_by_appname(self):
          '''
          test to check if we can find a user by appname and display information
           '''

          self.new_user.save_user()
          test_user = User("Grace","Graceeru","Gmail") # new contact
          test_user.save_user()

          found_user = User.find_by_name("Gmail")
                 
          self.assertEqual(found_user.appname,test_user.appname)
        
# check if a user object actually exists.
        def test_user_exists(self):
            '''
             test to check if we can return a Boolean  if we cannot find the contact.
            '''

            self.new_user.save_user()
            test_user = User("Grace","Graceeru","Gmail") # new contact
            test_user.save_user()

            user_exists = User.user_exist("Grace")

            self.assertTrue(user_exists)

# display all users
        def test_display_all_users(self):
             '''
             method that returns a list of all contacts saved
             '''

             self.assertEqual(User.display_user(),User.user_list)

        # def test_copy_username(self):
        #       '''
        #         Test to confirm that we are copying the user name from a found user
        #      '''

        #       self.new_user.save_user()
        #       User.copy_username("Grace")

        #       self.assertEqual(self.new_user.user_name,pyperclip.paste())




        
if __name__ == '__main__':
    unittest.main()