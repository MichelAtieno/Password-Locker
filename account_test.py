import unittest # Importing the unittest module
from account import Credentials # Importing the credentials class

class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args: 
       unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Credentials("Michel","Atieno","mishqamish@gmail.com","michel") #create new object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.first_name,"Michel")
        self.assertEqual(self.new_account.last_name,"Atieno")
        self.assertEqual(self.new_account.email,"mishqamish@gmail.com") 
        self.assertEqual(self.new_account.password,"michel")


if __name__ == '__main__':
    unittest.main()