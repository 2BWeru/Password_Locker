print(f'''Hello there, welcome to Password locker''''')

print(f''"please Input your user name and password to log in:")


# password locker details
# username_main = "Susans"
# password_main = "234567"
username_main = input()
password_main = input()

print(f"Hello {username_main}. what would you like to do?")
print('\n')

while True:
      print("Use these numbers : 1 - create a new UserDetails, 2 - display User details, 3 -find a user detail, 4 -exit the User details ")

      numbers = input()

      if numbers == '1':
          print("New User Details")
          print("-"*15)

          print ("User name ....")
          user_names = input()

          print("Password ...")
          pass_word = input()

          print("App name ...")
          app_name = input()

# display user
      elif numbers == '2':

         if display_user():
            print("Here is a list of all your User details")
            print('\n')

            for user in display_users():
               print(f"{user.user_names} {user.pass_word} .....{user.app_name}")

               print('\n')
         else:
               print('\n')
               print("You dont seem to have any contacts saved yet")
               print('\n')

# check existing user details
      elif numbers == '3':
                print("Enter the number you want to search for")
                search_number = input()
                if check_existing_contacts(search_number):
                  search_contact = find_contact(search_number)
                  print(f"{search_contact.first_name} {search_contact.last_name}")
                  print('-' * 20)

                  print(f"Phone number.......{search_contact.phone_number}")
                  print(f"Email address.......{search_contact.email}")
                else:
                  print("That contact does not exist")
      elif numbers == "4":
                   print("Bye .......")
                   break
else:
            print("I really didn't get that. Please use the short codes")
   # lets create User Class
