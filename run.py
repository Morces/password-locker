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

def display_user(user):
    '''
    Function that displays all users
    '''

    return User.display_user()

def save_user(user):
    '''
    Function for saving a new user
    '''

    user.save_user()

def delete_user(user):
    '''
    Function for deleting a user
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
                confirm_password = input
