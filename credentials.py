import pyperclip
class Credentials():
    def __init__(self,user_name,pass_word,appname):
       self.user_name = user_name
       self.pass_word = pass_word
       self.appname = appname

 # for the 2 test case
    def  save_credentials(self):

             
             Credentials.credentials_list.append(self)
        
    def delete_credentials(self):

        '''
        delete_user method deletes a saved user detail from the user_list
        '''

        Credentials.credentials_list.remove(self)

        # for  fourth test case
# to find user detail@classmethod
    @classmethod
    def find_by_name(cls,string):


        for credentials in cls.credentials_list:
         if credentials.appname == string:
                return credentials

# check if user detail exists
    @classmethod
    def credentials_exist(cls,name):
        
          '''
        Method that checks if a user details exists from the credentials list.
        Args:
            number: appname to search if it exists
        Returns :
            Boolean: True or false depending if the Account detail exists
        '''
          for credentials in cls.credentials_list:
                if credentials.appname == name:
                    return True

          return True

    @classmethod
    def display_credentials(cls):
          '''
        method that returns the credantial list
          '''
          return cls.credentials_list
        
    # @classmethod
    # def copy_username(cls,name):
    #     user_found = User.find_by_name(name)
    #     pyperclip.copy(user_found.user_name)




    # def delete_user(self):

    #      '''
    #     delete_contact method deletes a saved contact from the contact_list
    #     '''

    #      User.user_list.remove(self)


