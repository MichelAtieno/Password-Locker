import pyperclip

class Credentials: 
  ''' 
  Class that generates new instances of accounts
  '''
  account_list=[] #Empty account_list 

  def __init__(self, first_name,last_name,email,password):

      self.first_name = first_name
      self.last_name = last_name
      self.email = email
      self.password = password

  def save_account(self):
       '''
       save_account method saves credential objects into account_list
       '''

       Credentials.account_list.append(self)

  def delete_account(self):
      '''
      deletes a saved account from account_list
      '''

      Credentials.account_list.remove(self)

  @classmethod
  def authenticate_account(cls, first_name, password):
      '''
      Method that verifies user and password
      '''

      for account in cls.account_list:
          if account.first_name == first_name and account.password == password:
              return account
   
  @classmethod 
  def display_accounts(cls):
        '''
        method that returns the account list
        '''
       
        return cls.account_list
  
 # @classmethod
  #def copy_email(cls, first_name, password):
   #     contact_found = Credentials.authenticate_account(first_name, password)
    #    pyperclip.copy(accont_found.email)


class UserData:
    '''
    Class that holds user and website information
    '''

    userdata_list = []

    def __init__ (self,website,webpass):

        self.website = website
        self.webpass = webpass

   

