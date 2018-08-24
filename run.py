#!/usr/bin/env python3.6
from account import Credentials

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

def display_accounts():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_accounts()


def main():
    print("Hello Welcome to your account list. What is your name?")
    first_name = input()

    print(f"Hello {first_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : ca - create a new account, da - display account, aa -authenticate account, ex -exit the account list ")

                    short_code = input().lower()

                    if short_code == 'ca':
                            print("New Account")
                            print("-"*10)

                            print ("First name ....")
                            first_name = input()

                            print("Last name ...")
                            last_name = input()

                            print("Email address ...")
                            email = input()

                            print("Password ...")
                            password = input()


                            save_account(create_account(first_name,last_name,email,password)) # create and save new contact.
                            print ('\n')
                            print(f"New Account {first_name} {last_name} created")
                            print ('\n')

                    elif short_code == 'da':

                            if display_accounts():
                                    print("Here is a list of all your accounts")
                                    print('\n')

                                    for account in display_accounts():
                                            print(f"{account.first_name} {account.last_name} .....{account.email}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any accounts saved yet")
                                    print('\n')

                    elif short_code == 'aa':

                            print("Enter the account you want to search for")

                            search_first_name = input()
                            if check_existing_accounts(search_first_name):
                                    search_account = find_account(search_first_name)
                                    print(f"{search_account.first_name} {search_account.last_name}")
                                    print('-' * 20)
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That accountt does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()
