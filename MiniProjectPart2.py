import MiniProjectPart1
import re

listofusers = []
def createaccount():
    username = ""
    while validateusername(username) == False:
        username = input("Please enter a username for the account:\n").strip()
    password = ""
    while validatepassword(password) == False:
        password = input("Please enter the password for the account:\n")
    email = ""
    while validateemail(email):
        email = input("Please enter your email:\n")
    
def validateemail(email):
    if re.search(r"$(\w |(-|_|\.)(\w))+@[A-Za-z](\w |-\w)+\.[A-Za-z]{2,}", email) == None:
        return False
    return email
        
def validateusername(username):
    if re.search(r"[\w\.-]{5, }", username) == None:
        print("The username contains invalid character or is of the incorrect length.")
        return False
    return username

def validatepassword(password):
    if re.search(r"[\w\.\+-*=#\(\)&!?%]{8, }"):
        print("The password is invalid because it is too short or contains invalid characters.")
        return False
    return password

    