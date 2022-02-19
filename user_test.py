

import unittest
# importing unitest module


from credential import  Credentials
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
        self.new_user=User()

