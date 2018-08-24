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
  
 # @classmethod
  #def copy_email(cls, first_name, password):
   #     contact_found = Credentials.authenticate_account(first_name, password)
    #    pyperclip.copy(accont_found.email)


class UserData:
    '''
    Class that holds user and website information
    '''

    userdata_list = []

    def __init__ (self,username,website,webpass):

        self.username = username
        self.website = website
        self.webpass = webpass

    def save_website(self):
        '''
        create a method that saves website and password
        '''

        UserData.userdata_list.append(self)

    @classmethod 
    def display_userdata(cls, username, website):
        '''
        displays passwords from user
        '''
        for password in cls.userdata_list:
            if password.username == username:
                if password.website == website:
                    return password

    
    @classmethod
    def existing_userdata(cls, username):
        '''
        Checks if data exists in profile
        '''
        for userdata in cls.userdata_list:
            if userdata.username == username:
                return True
                return False

