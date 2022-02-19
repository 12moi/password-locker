

from typing_extensions import Self


class Credentials():
    '''
     
    Create credentials class to help create new objects of credentials
    
    '''

    acounts = []

    @classmethod
    def verify_user(cls, username,password):
        '''
        A method that very the user if the user exist in the user_list
        '''
        a_user=""
        for user in user.user_list:
            if(username==username and password==password):
                a_user=username
        return a_user
    
    def __init__(self,account,username, password):
           '''
           a method that defines the user credentials to saved
           '''
           self.account=account
           self.username=username
           self.password=password

    def save_credentials(self):
        '''
        save_user method saves a new user objects to the user_list
        '''
        Credentials.credentials_list.append(self)  

    def delete_credentils(self):
         '''
         A method that deletes a saved account from the list
         '''
         Credentials.credentials_list.remove(self) 

    @classmethod

    def find_credentials(cls, account):
        '''
        method that take account and retrieves password for the account
        '''
        for credential in cls.credentials_list:
            if credential.account==account:
                return credential
    
    @classmethod
    def display_credentials(cls):
        '''
        A method that returns all the items in the credentials list
        '''

        return cls.credentials_list