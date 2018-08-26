import pyperclip

class Credentials: 
  ''' 
  Class that generates new instances of accounts
  '''
  account_list=[] #Empty account_list 

  def __init__(self,user_id,first_name,last_name,email,password):
      
      self.user_id = user_id
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
      return 0
  
 # @classmethod
  #def copy_email(cls, first_name, password):
   #     contact_found = Credentials.authenticate_account(first_name, password)
    #    pyperclip.copy(accont_found.email)


class UserData:
    '''
    Class that holds user and website information
    '''

    userdata_list = []

    def __init__ (self,id,username,website,webpass):

        self.id = id
        self.username = username 
        self.website = website
        self.webpass = webpass

    def save_website(self):
        '''
        create a method that saves website and password
        '''

        UserData.userdata_list.append(self)

    @classmethod 
    def display_userdata(cls, number, count):
        '''
        displays passwords from user
        '''
        for password in cls.userdata_list:
            if password.id == number:
                if password.username == count:
                    return password

    
    @classmethod
    def existing_userdata(cls, number):
        '''
        Checks if data exists in profile
        '''
        for userdata in cls.userdata_list:
            if userdata.id == number:
                return True
                return False

    @classmethod 
    def copy_pass(cls,number,count):
        found_password = UserData.display_userdata(number,count)
        pyperclip.copy(found_password.webpass)

