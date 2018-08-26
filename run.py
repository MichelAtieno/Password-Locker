#!/usr/bin/env python3.6
from account import Credentials
import string, random, time

def create_account(first_name,last_name,email,password):
    '''
    Function to create a new account
    '''
    new_account = Credentials(first_name,last_name,email,password)
    return new_account

def save_account(account):
    '''
    Function to save account
    '''
    contact.save_account()

def del_account(account):
    '''
    Function to delete an account
    '''
    contact.delete_account()

def authenticate_account(first_name, password):
    '''
    Function to delete a contact
    '''
    account.authenticate_account()


def new_userdata(username, website, webpass):
    '''
    Function that creates new userdata
    '''
    new_userdata = UserData(username, website, webpass)
    return new_userdata

def save_userdata(userdata):
    '''
    Function that saves new userdata
    '''
    userdata.save_website()


def display_userdata():
    '''
    Function that displays user data
    '''
    return UserData.display_userdata(username, website)

def userdata_existing(userdata):
    '''
    Function that checks if userdata exists 
    '''
    return UserData.existing_userdata(userdata)
    
def webpass_generator(count):
    '''
    Function that generates password
    '''
    webpass_list=[]
    round = 1
    while round <= count:
        gen_password = random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
        webpass_list.append(gen_password)
        round+=1
    return ''.join(webpass_list)


def main():
    '''
    Executing Function
    '''
    user_id=0

    user_input = []

    print('\n')
    print("Hello Welcome to Password-locker")
    print("-"*40)
    while True:
        print('Type:\n ca to create new account\n si to sign-in\n ex to exit')
        selected_type = input().lower().strip()
        if selected_type == 'ca':
            print('Create Account:'+'\n'+'-'*25+'\n Enter Account-Name:')
            user_name = input('Account-Name: ')
            print('Enter password: ')
            pass_word = input('Password: ')

            print('\n')
            new_user(created_account(user_id,user_name,pass_word))
            user_id+=1 
            print(f'Account {user_name} has been created. \n Login to Continue')
            user_input.append(0)
            print('-'*25)   
    
if __name__ == '__main__':

    main()
