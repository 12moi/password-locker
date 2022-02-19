
from collections import UserList


class User:
    '''
    class that generates a new user instance
    '''
    user_list=[]
    def __init__(self, user_name, password):
        self.user_name=user_name
        self.password=password
    
    def save_user(self):
        '''
        save_user method saves a new user objects to the user_list
        '''
        User.user_list.append(self)
    
    @classmethod
    def diplay_user(cls):
        return cls.user_list
    def delete_user(self):
         '''
         A method that deletes a saved account from the list
         '''
         UserList.user_list.remove(self)
        
        
