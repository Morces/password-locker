import random
import string
from account import User

def create_user(username, password):
    '''
    This function creates a new user
    '''
    new_user = User(username, password)
    return new_user

