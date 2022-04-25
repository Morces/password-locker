#!/usr/bin/env python3.8

import random
import string
from account import User

def create_user(username, password):
    '''
    This function creates a new user
    '''
    new_user = User(username, password)
    return new_user

def display_user():
    '''
    Function that displays all users
    '''

    return User.display_user()

def save_user(user):
    '''
    Function for saving a new user
    '''

    user.save_user()

def del_user(user):
    '''
    Function for deleting a user account
    '''

    user.delete_user()

def find_user(username):
    '''
    Function for finding a user
    '''

    return User.find_username(username)

def existing_users(username):
    '''
    Checks for existing users
    '''

    return User.user_exist(username)


def main():
    print("Hello and Welcome to Password Locker. I hope you enjoy this application!")
    print('\n')

    while True:
        print("Nagivate using short codes. To create a new user, use 'cu', To display users, use 'du', To find a user, use 'fu', To delete user use 'dl', To exit user use 'ex'")

        short_code = input().lower()

        if short_code == 'cu':
            print("Create a username")
            created_username = input()
            print("Suggest password? Enter 'yes'")
            yes = input()
            if yes == "yes":
                pass_word = string.ascii_letters
                create_password = "".join(random.choice(pass_word) for i in range(10))
                print("Password successfully generated!")
                continue

            else:
                print("Create password")
                create_password = input()

                print("Confirm password")
                confirm_password = input()

            while create_password != confirm_password:
                print("Password does not match!")
                print("Retype your password")
                create_password = input()
                confirm_password = input()

            else:
                print(f"Welcome {created_username}. You have successfully created an account")
                save_user(create_user(created_username, create_password))
                print("\n")
        
        elif short_code == 'du':
            if display_user():
                print("This are all users")
                print("\n")

                for user in display_user():
                    print(f"{user.username}")
                    print("\n")

            else:
                print("\/n")
                print("You do not have any users saved yet.")
                print("\n")

        elif short_code == 'fu':
            print("Enter the username you want to find")
            search_user = input()

            if existing_users(search_user):
                searched_user = find_user(search_user)
                print(f"{searched_user.username}")
                print('-' * 20)
            else:
                print("This user does not exist!")

        elif short_code == 'dl':
            print("Enter 'yes' to delete this account")
            yes = input()
            if yes == 'yes':
                del_user(searched_user)
                print("Account deleted!")
            else:
                print("Couldn't find this account")

        elif short_code == 'ex':
            break
        else:
            print("Enter a valid code!")

if __name__ == '__main__':
    main()
            
