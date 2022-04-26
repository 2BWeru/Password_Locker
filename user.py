class User():
    def __init__(self,user_name,pass_word,app_name):
       self.user_name = user_name
       self.pass_word = pass_word
       self.app_name = app_name

    user_list = []
    # for the 2 test case
    def save_user(self):

             
             User.user_list.append(self)
            # for  third test case
    