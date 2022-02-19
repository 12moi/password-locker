

from typing_extensions import Self

from run import delete_account


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
    
    def __init__(self,accountname,accountusername, accountpassword):
           '''
           a method that defines the user credentials to saved
           '''
           self.accountname=accountname
           self.accountusername=accountusername
           self.accountpassword=accountpassword

    def save_account(self):
        '''
        this is a method that saves Accounts information
        '''
        Credentials.acounts.append(self)

        delete_account(self)
        '''
        Deletes saved account credentials
        '''
        Credentials.acounts.remove(self)

    @classmethod
    def display_accounts(cls):
        '''
        this method returns the accounts list
        '''
        for acount in cls.acounts:
            return cls.acounts

    @classmethod
    def find_by_number(cls,number):
        '''
        This method takes in a number and finds a contact that matches the number
        '''
        for account in cls.acounts:
            if account.accountusername==number:
                return account

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