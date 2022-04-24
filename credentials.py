import random
import string


class Credentials:

    '''
    This class generates new instances of credentials
    '''
    credentials_list = []

    def __init__(self, account_username, account_password):

        '''
        function that defines object properties
        '''

        self.account_username = account_username
        self.account_password = account_password

    def delete_credentials(self):

        '''
        This method deletes the credential object
        '''

        Credentials.credentials_list.remove(self)