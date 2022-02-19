
import string

from user import User

from credential import Credentials

def create_user(self,username,password):

    new_user=User(self, username,password)
    return new_user


def save_user(user):
   user.save_user
def delete_user(user):
   user.delete_user

def find_user(username):
   return User.find_by_username(username)

def display_users():
    return User.diplay_users()
