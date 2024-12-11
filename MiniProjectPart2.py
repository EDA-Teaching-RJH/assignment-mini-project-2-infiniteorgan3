import MiniProjectPart1
import re
import csv

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
    attempts = 3
    while validatepassword(password) == None and attempts > 0:
        password = input("Please enter the password for the account:\n")
        attempts -= 1
    email = ""
    attempts = 3
    while validateemail(email) == None and attempts > 0:
        email = input("Please enter your email:\n")
        attempts -= 1
    try:
        newuser = MiniProjectPart1.UserAccount(username, password, email, listofusers)
    except ValueError:
        print("The user account could not be created, please try again.")
    else:
        listofusers.append(newuser)
    
def saveaccounts():
    with open("accounttext.txt", "a") as writer:
        with open("accounttext.txt", "r") as reader:
            lines = reader.read()
        for i in listofusers:
            if i in lines:
                pass
            else:
                writer.append(i)
                
                
    with open("allaccountinfo.csv","")
    print("All of the accounts' information has been saved.")

def deleteaccount(userid):
    attemptedresultreturn = [account for account in listofusers if account.userid == userid]
    if attemptedresultreturn != []:
        listofusers.remove(attemptedresultreturn)
        with open("accounttext.txt", "w") as writer:
            for i in listofusers:
                writer.write(i)
                
def searchforaccount(username):
    pattern = r"$" + username
    with open("accounttext.txt", "r") as reader:
        filestring = reader.read()
    matches = re.findall(pattern, filestring)
    if len(matches) == 0:
        print("There are no matches found with the search.")
    else:
        print("The found users are:")
        for i in matches:
            print(i)   
    
def validateemail(email):
    if re.search(r"$(\w|(-|_|\.)(\w))+@[A-Za-z](\w |(-|\.)\w)+\.[A-Za-z]{2,}^", email) == None:
        print("This email has an invalid format.")
        return None
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
    if re.search(r"[\w\.\+-*=#\(\)&!?%]{8, }"):
        print("The password is invalid because it is too short or contains invalid characters.")
        return None
    return password

def saveoneaccount():

def main():
    continuation = True
    while continuation == True:
        validchoices = ["create","search","delete","save all", "save one"]
        print("Welcome to the program to save and create user accounts, the options for utilising the program are:\n1. Creating a New Account.\n2. Searching for a user account.\n3. Deleting a user account.\n4. Saving all of the accounts to a file.\n5. Saving the information of one account.")
        inputchoice = ""
        attempts = 3
        while inputchoice not in validchoices and attempts > 0:
            inputchoice = input("What would you like to do?").lower().strip()
        if attempts == 0:
            print("No request was made and so the program will close.")
            break
        match inputchoice:
            case "create":
                createaccount()
            case "search":
                # add code
                searchforaccount()
            case "delete":
                # delete
                deleteaccount()
            case "save all":
                saveaccounts()
            case "save one":
                # add code
                saveoneaccount()
            
        

if __name__ == "__main__":
    main()