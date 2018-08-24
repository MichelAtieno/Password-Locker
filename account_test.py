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

    def test_save_account(self):
        '''
        test_save_account test case to test if the credential object is saved into the account list
        '''
        self.new_account.save_account() #saving new account
        self.assertEqual(len(Credentials.account_list),1)


if __name__ == '__main__':
    unittest.main()