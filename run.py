from user import User
from credentials import Credentials
# main

def main():
    print("Hello Welcome to your Password locker.")
    print(" What is your name?")
    login = input()
    

    print(f"Hello {login}. lets help you log in ?")
    print('\n')
    print(f" Do yo want to :")
    print(f" A. - Generate password : ")
    print(f" B. - Type password : ")
    answ = input()
    if (answ == "A"):
        # Save
        print(f" Your Password is : 45678")
        
    elif ( answ == "B"):
        input("Password : ")
        print('\n')
        
        
    while True:
      print('\n')
      print(f"{login} Select choice of action , by  using the numbers/ shortcode next to it:" )
      print('\n')
      print("1 - create a new Account Details.")
      print("2 - display Account details.")
      print("3 - find an Account details.")
      print("ex - exit the current Account detail.")
      print("4 - delete user Account details.")
      print('\n')
      short_code = input().lower()

      if short_code == '1':
         print("New Account Details")
         print("-"*10)

         print ("User name ....")
         user_name = input()

         print("Password ...")
         pass_word = input()

         print("App name ...")
         app_name = input()

         save_user(create_user(user_name ,pass_word, app_name)) # create and save new contact.
         print ('\n')
         print(f"New Account details {user_name} ,{pass_word} ,{app_name} created")
         print ('\n')

      elif short_code == '2':
         details = display_user()
        #  list_present = createDatalist()
         if len(details) != 0 :
            print("Here is a list of all your Account details")
            print('\n')

            for index,user in enumerate(details):
               print(f"{index+1}. {user.user_name}, {user.appname},{user.pass_word}")
               print(f"{user.user_list}")

               print('\n')
         else:
               print('\n')
               print("You dont seem to have any Account details saved yet")
               print('\n')

      elif short_code == '3':

               print("Enter the  App name you want to search for")

               search_app_name = input()
               if find_user(search_app_name):
                   search_app_name = find_user(search_app_name)
                   print(f"{search_app_name.appname}")
                   print('-' * 20)

                   print(f"Username.......{search_app_name.user_name}")
                   print(f"Password.......{search_app_name.pass_word}")
               else:
                   print("That Account detail does not exist")
      elif  short_code == "4":
                   print("Are you sure you want to delete this Account detail")
                   print("Enter the Account's app name you want to delete")
                   search_user_name = input()
                   if find_user(search_user_name):
                    search_user_name = find_user(search_user_name)
                    print(f"{search_user_name.user_name} {search_user_name.pass_word}")
                    print('-' * 20)
                    search_user_name.delete_user()
                    print("\n")
                    print(f"Your  Account  detail is : {search_user_name.user_name} successfully deleted!")
                    print('\n')
                   else:
                     print("User Account detail cannot be found")


      elif short_code == "ex":
                 print("Bye .......")
                 break
      else:
                     print("I really didn't get that. Please use the short code / numbers")
                     print("unable to log in")

               
   
     
      
         
# end of main
# Create a new user
def create_user(user_name,pass_word,app_name):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,pass_word,app_name)
    return new_user
    # existing list

# save user
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

# deletes user
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

# find user if it exists
def find_user(name):
    '''
    Function that finds a user by name and returns the username
    '''
    return User.find_by_name(name)

# check if user exists
def check_existing_user(name):
    '''
    Function that check if a users exists with that number and return a Boolean
    '''
    return User.user_exist(name)

# display users
def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()


if __name__ == '__main__':
 main()