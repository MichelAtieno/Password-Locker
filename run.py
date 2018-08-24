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
