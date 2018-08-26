import unittest # Importing the unittest module
from account import Credentials,  UserData # Importing the credentials class
import pyperclip

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
        self.new_account = Credentials(1,"Michel","Atieno","mishqamish@gmail.com","michel") #create new object
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        Credentials.account_list = []



    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.user_id,1)
        self.assertEqual(self.new_account.first_name,"Michel")
        self.assertEqual(self.new_account.last_name,"Atieno")
        self.assertEqual(self.new_account.email,"mishqamish@gmail.com") 
        self.assertEqual(self.new_account.password,"michel")

    def test_save_account(self):
        '''
        tests case to test if the credential object is saved into the account list
        '''
        self.new_account.save_account() #saving new account
        self.assertEqual(len(Credentials.account_list),1)

    def test_save_multiple_accounts(self):
        '''
        tests to check if we can solve multiple credential objects to our account_list
        '''
        self.new_account.save_account()
        test_account = Credentials(1,"Jerusha","Auma","jeruauma@gmail.com", "jeru") #new account
        test_account.save_account()
        self.assertEqual(len(Credentials.account_list),2)

    def test_delete_account(self):
        '''
        tests if we can remove an account from account_list
        '''
        self.new_account.save_account()
        test_account = Credentials(1,"Jerusha","Auma","jeruauma@gmail.com", "jeru")
        test_account.save_account()

        self.new_account.delete_account() #Deleting a credential object
        self.assertEqual(len(Credentials.account_list),1)

    def test_auhenticate(self):
        '''
        test to check if we can restrict access by password authentication
        '''

        self.new_account.save_account()
        test_account = Credentials(1,"Jerusha","Auma","jeruauma@gmail.com", "jeru")
        test_account.save_account()

        found_account = Credentials.authenticate_account("Jerusha","jeru")
        self.assertEqual(found_account.user_id, test_account.user_id)

class TestUserData(unittest.TestCase):

    def setUp(self):
    
        '''
        Set up method to run before each test cases.
        '''
        self.new_userdata = UserData(1,"Michel","twitter.com","yolo")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        UserData.userdata_list = []
    
    def test_init(self):

        '''
        Test class that defines test case for website and logging in
        '''
        self.assertEqual(self.new_userdata.id, 1)
        self.assertEqual(self.new_userdata.username,"Michel")
        self.assertEqual(self.new_userdata.website,"twitter.com")
        self.assertEqual(self.new_userdata.webpass,"yolo")

    def test_save_website(self):
        '''
        tests case to test if website and webpass can be saved
        '''

        self.new_userdata.save_website() #saving new website
        self.assertEqual(len(UserData.userdata_list),1)

    def test_display_userdata(self):
        '''
        method that returns a list of all websites saved
        '''
        self.new_userdata.save_website()
        test_userdata = UserData(1,"Michel","twitter.com","yolo")
        test_userdata.save_website()

        userdata_found = UserData.display_userdata(1,"Michel")
        self.assertEqual(userdata_found.website, test_userdata.website)

    def test_userdata_exists(self):
        '''
        Testing if method for checking userdata works
        '''
        self.new_userdata.save_website()
        test_userdata = UserData(1,"Michel","twitter.com","yolo")
        test_userdata.save_website()

        userdata_exists = UserData.existing_userdata("Michel")
        self.assertTrue(userdata_exists)

    def test_copy_pass(self):
        '''
        Testing if password has been copied
        '''
        self.new_userdata.save_website()
        UserData.copy_pass(1,"Michel")

        self.assertEqual(self.new_userdata.webpass,pyperclip.paste())



    


if __name__ == '__main__':
    unittest.main()