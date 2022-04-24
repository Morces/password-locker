class User:
    '''
    Class which generates new user instances
    '''
    user_list = []

    # constructor for username and password

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):

        '''
        This method saves an instance of a user in the user list
        '''

        User.user_list.append(self)

    
