

import unittest

import pyperclip



from user import  Credentials
# importing credentials class

from user import User
# importing user class

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    
    
    def setUp(self):
        '''
        A method that runs before test method runs
        '''
        self.new_user=User('moi', 'shadrack', 'shadrack12')

    
    
    def test_init(self):
        '''
        This test checks if the object has been initialized correctly
        '''
       
        self.assertEqual(self.new_user.username,'mosha')
        self.assertEqual(self.new_user.password, 'mosha12')


    def test_save_user(self):
        '''
       A  test case to test if a new user instance has been saved into the User list
        '''    
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        '''
        A method that runs before test method runs
        '''
        self.new_credential=Credentials('accountname','accountusername','accountpassword')
    
    def test_init(self):
        '''
        A test case to check if the credentials  has been initialized correctly
        '''
        self.assertEqual(self.new_credential.accountname, 'facebook')
        self.assertEqual(self.new_credential.accountusername, 'mosha')
        self.assertEqual(self.new_credential.accountpassword, 'mosha12')
    
    def save_credential_test(self):
        '''
        The test case for credentials object if saved to credential_list or not
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
        This is method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    

    def test_delete_credential(self):
        """
        test method is a method that test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_account()
        test_credential = Credentials("Twitter","mosha21","21mosha")
        test_credential.save_account()

        

    def test_find_credentials(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential.save_account()
        test_credential = Credentials("Twitter","mosha21","21mosha") 
        test_credential.save_account()

        the_credential = Credentials.find_credentials("Twitter")

       

    def test_display_all_saved_credentials(self):
        '''
        method that displays all the credentials that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    

   

if_name_="_main_"
unittest.main()
        
