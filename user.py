import pyperclip
class User():
    user_list = []

    def __init__(self,user_name,pass_word,appname):
       self.user_name = user_name
       self.pass_word = pass_word
       self.appname = appname
    
    @classmethod
    def createDatalist(cls):
        cls.user_list = [
         cls("Mitch2","23Mitch","Twitter"),
         cls("lucy","99Lu","TikTok"),
         cls("Kev","kev45","Spotify")
        ]
        return User.createDatalist()
        
    # for the 2 test case
    def save_user(self):

             
             User.user_list.append(self)
        
    def delete_user(self):

        '''
        delete_user method deletes a saved user detail from the user_list
        '''

        User.user_list.remove(self)

        # for  fourth test case
# to find user detail@classmethod
    @classmethod
    def find_by_name(cls,string):


        for user in cls.user_list:
         if user.appname == string:
                return user

# check if user detail exists
    @classmethod
    def user_exist(cls,name):
        
          '''
        Method that checks if a user details exists from the user list.
        Args:
            number: appname to search if it exists
        Returns :
            Boolean: True or false depending if the user detail exists
        '''
          for user in cls.user_list:
                if user.appname == name:
                    return True

          return True

    @classmethod
    def display_user(cls):
          '''
        method that returns the user list
          '''
          return cls.user_list
        
    # @classmethod
    # def copy_username(cls,name):
    #     user_found = User.find_by_name(name)
    #     pyperclip.copy(user_found.user_name)




    # def delete_user(self):

    #      '''
    #     delete_contact method deletes a saved contact from the contact_list
    #     '''

    #      User.user_list.remove(self)

