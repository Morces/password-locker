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
    print("")
