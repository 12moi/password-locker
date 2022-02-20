
import string


import pyperclip

from user import User

from user import Credentials

def create_user(self,firstname,lastname,username,userpassword):

    new_user=User(self,firstname,lastname, username,userpassword)
    return new_user


def save_user(user):
   user.save_user
def delete_user(user):
   user.delete_user

def find_user(username):
   return User.find_by_username(username)

def display_users():
    return User.diplay_users()

def create_account(accountusername,accountname,accountpassword):
    newaccount=Credentials(accountusername,accountpassword)

def save_account(user):
    user.save_account()

def find_account(number):
    return Credentials.find_by_number(number)
def display_accounts():
    return Credentials.dispaly_accounts()

def delete_account(user):
    user.delete_account()

def copy_credential():
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credentials.copy_credential()


def main():
       while True:
           print("Welcome to Password locker type SU or LG to get started")
           print("SU -or- LG")
           option=input()
           if option=="SU":
               print("Create Account")
               print("-"*10)
               print("Enter your username...")
               username=input()
               print("Enter your username...")
               print("Set your password...")
               userpassword=input()
               save_user(create_user(username,userpassword))
               print("Your userpassword was created successful. Below are your details:")
               print("-"*10)
               print(f"Name:\nUsername:{username}\nPassword:{userpassword}")

            #   firstname,lastname,
            #    {firstname} {lastname}

               print("\n \n")
           elif option=="LG":
               print("Your username...")
               username=input()
               print("Your password...")
               loginPassword=input()
               if find_user(loginPassword):
                   print("\n")
                   print("You can add many accounts (AC) and also view them (VC) ")
                   print("-"*60)
                   print("AC -or-VC")
                   choose=input()
                   print("\n")
                   if choose=="AC":
                       print("Add your Account credentials")
                       print("-"*25)
                       accountName=username
                       print("Account Name")
                       accountName=input()
                       print("\n")
                       print("Create new password for your account..")
                       print("\n")
                       print("Enter your password...")
                       accountpassword=input()
                       save_account(create_account(accountName,username,accountpassword))

                   elif choose=="VC":
                       if find_account(accountName):
                           print("Here is a list accounts you have created : ")
                           print("-"*25)
                           for user in display_accounts():
                               print(f"Account:{user.accountname} \nPassword:{user.accountpassword} \n\n")
                            
                       else:
                            print("Invalid credentials!")

                   else:
                       print("PLEASE TRY AGAIN!")
                       print("\n")
               else:
                    print("Incorrect information please try again! Thank you")
                    print("\n")
           else:
                print("Please choose a valid option")
                print("\n")
if_name_='_main_'
main()






