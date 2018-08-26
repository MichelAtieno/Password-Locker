#!/usr/bin/env python3.6
from account import Credentials
import string, random, time

def create_account(user_id,first_name,last_name,email,password):
    '''
    Function to create a new account
    '''
    new_account = Credentials(user_id,first_name,last_name,email,password)
    return new_account

def save_account(account):
    '''
    Function to save account
    '''
    account.save_account()

def del_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()

def authenticate_account(first_name, password):
    '''
    Function to authenticate account
    '''
    return Credentials.authenticate_account(first_name, password)


def new_userdata(id,username,website, webpass):
    '''
    Function that creates new userdata
    '''
    new_userdata = UserData(id, username, website, webpass)
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

def webpass_generator(id):
    '''
    Function that generates password
    '''
    webpass_list = []
    round = 1
    while round<=id:
        gen_password = random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase)
        webpass_list.append(gen_password)
        round+=1
    return ''.join(webpass_list)

def main():
    '''
    Executing Function
    '''
    my_id=0
    #id = 0
    user_input = []

    print('\n')
    print("Hello Welcome to Password-locker")
    print("-"*25)
    while True:
        print('Type:\n ca to create new account\n si to sign-in\n ex to exit')
        selected_type = input().lower().strip()
        if selected_type == 'ca':
            print('Create Account:'+'\n'+'-'*25+'\n Enter Account-Name:')
            new_first_name = input('Account-First-Name: ')
            new_last_name = input('Account-Last-Name: ')
            print('Enter email: ')
            new_email = input('Account-Email: ')
            print('Enter password: ')
            pass_word = input('Password: ')

            print('\n')
            save_account(create_account(my_id,new_first_name,new_last_name,new_email,pass_word))
            my_id+=1 
            print(f'Account {new_first_name} {new_last_name} has been created. \n Login to Continue')
            user_input.append(0)
            print('-'*25)

        elif selected_type == 'si':
            print('Enter Account-Name and Password to continue:')
            user_login = input('Account-Name: ')
            user_webpass = input('Password: ')
            user_signin = authenticate_account(user_login,user_webpass)
            if user_signin == 0:
                print('\n')
                print('Invalid Account-Name and/or Password')
                print('-'*25)

            elif user_signin != 0:
                print('\n')
                print('Welcome {user-signin.first_name}')
                while True:
                    print('Type:\n cp - Create Password sp- Show Passwords cp - Copy Passwoyd to clipboard\n lo - Log out')
                    new_user_input = input().lower()
                    if new_user_input == 'cp':
                        print('Add Website and Password: ')
                        print('Enter Website: ')
                        new_website = input()
                        print('Length of Password: ')
                        password_length = int(input('Password Length: '))

                        #def webpass_generator(size=password_length, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
                        #    pwd = ''.join(random.choice(chars) for _ in range(size))
                         #   return pwd

                        #new_webpass = webpass_generator()

                        new_user_id = user-sign_in.user_id
                        save_userdata(new_userdata(new_user_id,user_input[new_user_id],new_website,new_webpass))
                        user_input[new_user_id] = user_input[new_user_id]+1
                        
                        print('\n')
                        print(f'Your password is {new_webpass}')
                        print('-'*25)

                    #elif new_user_input == 'sp':
                     #if userdata_existing(user_signin.first_name)
                        # length = user_input[user_signin.first_name]
                        # print(f'You have {length} passwords:')
                        # print('\n')
                         



                    

    
if __name__ == '__main__':

    main()
