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
        This method displays all users
        '''

        return cls.user_list

    
    @classmethod
    def find_username(cls, username):

        '''
        This method finds users using their usernames
        '''

        for user in cls.user_list:
            if user.username == username:
                return user
        

    @classmethod
    def user_exist(cls, username):
        '''
        This method checks if a given user exists
        '''
        for user in cls.user_exist:
            if user.username == username:
                return user

        

    
    

