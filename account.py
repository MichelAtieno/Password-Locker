class Credentials: 
  ''' 
  Class that generates new instances of accounts
  '''
  account_list=[]

  def __init__(self, first_name,last_name,email,password):

      self.first_name = first_name
      self.last_name = last_name
      self.email = email
      self.password = password