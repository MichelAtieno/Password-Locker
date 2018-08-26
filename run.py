#!/usr/bin/env python3.6
from account import Credentials
from account import UserData
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


def my_new_userdata(newuser_id, username, website, webpass):
    '''
    Function that creates new userdata
    '''
    new_userdata = UserData(newuser_id, username, website, webpass)
    return new_userdata

def save_userdata(userdata):
    '''
    Function that saves new userdata
    '''
    userdata.save_website()


def display_userdata(userdata, number):
    '''
    Function that displays user data
    '''
    return UserData.display_userdata(userdata, number)

def userdata_existing(userdata):
    '''
    Function that checks if userdata exists 
    '''
    return UserData.existing_userdata(userdata)

def copy_pass(number, count):
    '''
    Function that copies password to clipboard
    '''
    UserData.copy_pass(number, count)

def webpass_generator(count):
    '''
    Function that generates password
    '''
    webpass_list = []
    round = 1
    while round<=count:
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
            new_first_name = input('Account-First-Name: ').strip()
            new_last_name = input('Account-Last-Name: ').strip()

            print('Enter email: ')
            new_email = input('Account-Email: ').strip()

            print('Enter password: ')
            pass_word = input('Password: ').strip()

            print('\n')
            save_account(create_account(my_id,new_first_name,new_last_name,new_email,pass_word))
            my_id+=1

            print(f'Account {new_first_name} {new_last_name} has been created. \n Login to Continue')
            user_input.append(0)

            print('-'*25)

        elif selected_type == 'si':
            print('Enter Account-Name and Password to continue:')
            user_login = input('Account-Name: ').strip()
            user_webpass = input('Password: ').strip()
            user_signin = authenticate_account(user_login,user_webpass)
            if user_signin == 0:
                print('\n')
                print('Invalid Account-Name and/or Password')
                print('-'*25)

            elif user_signin != 0:
                print('\n')
                print(f'Welcome {user_signin.first_name}')
                while True:
                    print('Type:\n cp - Create Password sp- Show Passwords cop - Copy Password to clipboard\n lo - Log out')
                    new_user_input = input().lower()
                    if new_user_input == 'cp':
                        print('-'*25)
                        print('Add Website and Password: ')
                        print('Enter Website: ')
                        new_website = input()

                        print('Length of Password: ')
                        password_length = int(input('Password Length: '))
                        new_webpass = webpass_generator(password_length)
                        new_user_id = user_signin.user_id
                        save_userdata(my_new_userdata(new_user_id,user_input[new_user_id],new_website,new_webpass))
                        user_input[new_user_id] = user_input[new_user_id]+1
                        
                        print(f'Your password for {new_website} is {new_webpass}')
                        print('-'*25)

                    elif new_user_input == 'sp':
                     if userdata_existing(user_signin.user_id):
                         length = user_input[user_signin.user_id]
                         print(f'You have {length} passwords:')
                         print('\n')
                         my_user_data=0
                         while my_user_data < length:
                             get_pass = display_userdata(user_signin.user_id,my_user_data)
                             print(f'{my_user_data+1}. Your Password for {get_pass.website} is {get_pass.webpass}')
                             my_user_data+=1
                    

                         print('\n Enter new command')
                         print('-'*25)
                     else:
                          print('\n You have no registered accounts with passwords')
                          print('-'*25)

                    elif new_user_input == 'cop':
                     if userdata_existing(user_signin.user_id):
                         print('Enter index of password you want to copy:')
                         show_index = int(input('Enter index: '))-1
                         if show_index >= user_input[user_signin.user_id] or show_index<0:
                             print('\n')

                             print(f'{show_index+1} is invalid')
                             print('Enter sp to verify index of password')
                             print('-'*25)

                         elif show_index <user_input[user_signin.user_id]:
                                 copy_pass(user_signin.user_id,show_index)
                                 print('\n')
                                 print(f'The password for {show_index+1} has been copied')
                                 print('-'*25)
                     else:
                         print('No passwords')
                         print('-'*25)

                    elif new_user_input == 'lo':
                        print('\n')
                        print(f'Bye {user_signin.first_name}!')
                        print('-'*25)
                        break
                    else:
                         print('Invalid Entry')
                         print('-'*25)

            elif selected_type == 'ex':
                print('\n')
                print(f'Bye')
                print('-'*25)
                break

            else:
                print('Invalid entry')
                print('-'*25)
                    

    
if __name__ == '__main__':

    main()
