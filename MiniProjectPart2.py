import MiniProjectPart1
import re

listofusers = []
def createaccount():
    reasonsforinvalid = []
    attempts = 3
    username = ""
    while type(validateusername(username)) == list and attempts > 0:
        reasonsforinvalid = validateusername(username)
        if attempts != 3:
            for i in reasonsforinvalid:
                print(i)
        username = input("Please enter a username for the account:\n").strip()
        attempts -= 1
    password = ""
    while type(validatepassword(password)) == list and attempts > 0:
        reasonsforinvalid = validatepassword(password)
        if attempts != 3:
            for i in reasonsforinvalid:
                print(i)
        password = input("Please enter the password for the account:\n")
        attempts -= 1
    email = ""
    while type(validateemail(email)) == list and attempts > 0:
        reasonsforinvalid = validateemail(email)
        if attempts != 3:
            for i in reasonsforinvalid:
                print(i)
        email = input("Please enter your email:\n")
        attempts -= 1
    try:
        newuser = MiniProjectPart1.UserAccount(username, password, email, listofusers)
    except ValueError:
        print("The user account could not be created, please try again.")
    else:
        listofusers.append()
    
def saveaccounts():
    with open("accounttext.txt", "a") as writer:
        with open("accounttext.txt", "r") as reader:
            lines = reader.read()
        for i in listofusers:
            if i in lines:
                pass
            else:
                writer.append(i)
            
        
        
    
def validateemail(email):
    reasons = []
    if re.search(r"$(\w |(-|_|\.)(\w))+@[A-Za-z](\w |-\w)+\.[A-Za-z]{2,}", email) == None:
        reasons.append("This email has an invalid format.")
        return reasons
    return email
        
def validateusername(username):
    reasons = []
    if re.search(r"[\w\.-]{5, }", username) == None:
        if len(username) < 5:
            reasons.append("The username is too short.")
        if re.search(r"[^\w\.-]", username):
            reasons.append("The username contains invalid characters.")
        return reasons
    return username

def validatepassword(password):
    reasons = []
    if re.search(r"[\w\.\+-*=#\(\)&!?%]{8, }"):
        print("The password is invalid because it is too short or contains invalid characters.")
        return reasons
    return password

    