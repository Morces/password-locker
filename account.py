from requests import delete


class User:

    '''
    Class which generates new user instances
    '''
    user_list = []

    # constructor function for username and password

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):

        '''
        This method saves an instance of a user in the user list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        This method deletes an instance of a user in the user list
        '''

        User.user_list.remove(self)


    @classmethod
    def display_user(cls):

        '''
        This method takes in an application name and return a string that matches that name
        '''

        return cls.user_list

