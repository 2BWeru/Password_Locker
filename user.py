class User():
    def __init__(self,user_name,pass_word,appname):
       self.user_name = user_name
       self.pass_word = pass_word
       self.appname = appname

    user_list = []
    # for the 2 test case
    def save_user(self):

             
             User.user_list.append(self)
        
        # for  fourth test case
# to find user detail@classmethod
    @classmethod
    def find_by_name(cls,string):


        for user in cls.user_list:
         if user.appname == string:
                return user

        




    # def delete_user(self):

    #      '''
    #     delete_contact method deletes a saved contact from the contact_list
    #     '''

    #      User.user_list.remove(self)

