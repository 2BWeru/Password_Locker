from user import User
from credentials import Credentials
# main

def main():
    print("Hello Welcome to your Password locker.")
    print(" What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
      print("Use these short codes : ud - create a new UserDetails, dc - display user details, fc -find a user details, ex -exit the user details list ")

      short_code = input().lower()

      if short_code == 'ud':
         print("New User Details")
         print("-"*10)

         print ("User name ....")
         user_names = input()

         print("Password ...")
         pass_word = input()

         print("App name ...")
         app_name = input()

         save_user(create_user(user_name ,pass_word, app_name)) # create and save new contact.
         print ('\n')
         print(f"New User details {user_names} ,{pass_word} ,{app_name} created")
         print ('\n')

      elif short_code == 'dc':
         
         if display_user():
            print("Here is a list of all your User details")
            print('\n')

            for user in display_user():
               print("username" , "password", "appname")

               print('\n')
         else:
               print('\n')
               print("You dont seem to have any user details saved yet")
               print('\n')

      elif short_code == 'fc':

               print("Enter the App name you want to search for")

               search_name = input()
               if check_existing_user(search_name):
                   search_user = find_user(search_name)
                   print(f"{search_user.user_name} {search_user.pass_word}")
                   print('-' * 20)

                   print(f"Username.......{search_user.username}")
                   print(f"Password.......{search_user.pass_word}")
               else:
                   print("That User detail does not exist")

      elif short_code == "ex":
               print("Bye .......")
               break
      else:
               print("I really didn't get that. Please use the short codes")
# end of main
# Create a new user
def create_user(user_name,pass_word,app_name):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,pass_word,app_name)
    return new_user

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
    Function that finds a user by number and returns the contact
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