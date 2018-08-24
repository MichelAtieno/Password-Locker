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
