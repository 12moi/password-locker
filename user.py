



from collections import UserList

class User:
    '''
    class that generates a new user instance
    '''

    # Empty user list array
    user_list=[]
    def __init__(self,firstname,lastname, username, userpassword):
        self.username=username
        self.firstname=firstname
        self.lastname=lastname
        self.password=userpassword
    
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

    def   delete_account(self):
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
    def find_by_username(cls,username):
        '''
        This method takes in a number and finds a contact that matches the number
        '''
        for account in cls.acounts:
            if account.accountusername==username:
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
        
