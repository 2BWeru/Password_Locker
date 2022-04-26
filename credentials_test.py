
import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):
        '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
        
        def test_start(self):
                self.assertEqual(self.new_credentials.user_name,"bettyweru")
                self.assertEqual(self.new_credentials.pass_word,"b345")
                self.assertEqual(self.new_credentials.app_name,"Todolist")

 # second testcase
        def test_save(self):
            """
             to test if credentials are saved in the password locker
            """
    
            self.new_credentials.credentials_list() #saving the new credentials
            self.assertEqual(len(Credentials.credentials_list),1)
# third test case 
        def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

        def test_save_multiple_credentials(self):
            """
            test_save_multiple_user to save multiple user details
            """
            self.new_user.save_user()
            test_credentials = Credentials("Grace","Graceeru","Gmail") # new account detail
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)

# delete credentials details test
        def test_delete_credentials(self):
              '''
               test_delete_user to test if we can remove a contact from our contact list
              '''
              self.new_credentials.save_credentials()
              test_credentials = Credentials("Grace","Graceeru","Gmail") # new contact
              test_credentials.save_credentials()

              self.new_credentials.delete_credentials()# Deleting a contact object
              self.assertEqual(len(Credentials.credentials_list),1)
     
    #  to find app name

        def test_find_credentials_by_appname(self):
          '''
          test to check if we can find a user by appname and display information
           '''

          self.new_credentials.save_credentials()
          test_credentials = Credentials("Grace","Graceeru","Gmail") # new contact
          test_credentials.save_credentials()

          found_credentials = Credentials.find_by_name("Gmail")
                 
          self.assertEqual(found_credentials.appname,test_credentials.appname)
        
# check if a user object actually exists.
        def test_credentials_exists(self):
            '''
             test to check if we can return a Boolean  if we cannot find the Account details.
            '''

            self.new_credentials.save_credentials()
            test_credentials = Credentials("Grace","Graceeru","Gmail") # new contact
            test_credentials.save_credentials()

            credentials_exists = Credentials.credentials_exist("Grace")

            self.assertTrue(credentials_exists)

# display all credentials
        def test_display_all_credentialss(self):
             '''
             method that returns a list of all contacts saved
             '''

             self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

        # def test_copy_username(self):
        #       '''
        #         Test to confirm that we are copying the user name from a found user
        #      '''

        #       self.new_user.save_user()
        #       User.copy_username("Grace")

        #       self.assertEqual(self.new_user.user_name,pyperclip.paste())




        
if __name__ == '__main__':
    unittest.main()
  