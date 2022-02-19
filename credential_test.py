

import unittest

from credential import Credentials


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
        self.new_credential=Credentials()
    
    def test_init(self):
        '''
        A test case to check if the credentials  has been initialized correctly
        '''
        self.assertEqual(self.new_credential.account, '')
        self.assertEqual(self.new_credential.username, '')
        self.assertEqual(self.new_credential.password, '')
    
    def save_credential_test(self):
        '''
        The test case for credentials object if saved to credential_list or not
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)