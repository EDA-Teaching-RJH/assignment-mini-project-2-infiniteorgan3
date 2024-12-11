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
    typeaccount = None
    isstudent = False
    attempts = 3
    while typeaccount not in ["student", "unaffiliated"] and attempts > 0:
        typeaccount =  input("Are you a student or unaffiliated with the university?\n").lower().strip()
        attempts -= 1
    if attempts == 0:
        print("You did not enter a valid type of account.")
        return None
    match typeaccount:
        case "student":
            isstudent = True
        case "unaffiliated":
            isstudent = False        
    try:
        if isstudent == False:
            newuser = MiniProjectPart1.UserAccount(username, password, email, listofusers)
        else:
            coursesubject = input("What course are you studying?\n").upper().strip()
            newuser = MiniProjectPart1.StudentAccount(username, password, email, coursesubject, listofusers)
    except ValueError:
        print("The user account could not be created, please try again.")
    else:
        listofusers.append(newuser)
    
def saveaccounts():
    dataentries = ["UserID","Username","Email","Password"]
    rows= []
    for i in listofusers:
        rows.append([i.userid, i.username, i.email, i.password])
    
    with open("allaccountinfo.csv","w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataentries)
        csvwriter.writerows(rows)

    print("All of the accounts' information has been saved.")

def deleteaccount(userid):
    attemptedresultreturn = [account for account in listofusers if account.userid == userid]
    if attemptedresultreturn != []:
        listofusers.remove(attemptedresultreturn)
        saveaccounts()
                
def searchforaccount(username):
    usernamelist = []
    try:
        file = open("allaccountinfo.csv", "r")
        reader = csv.reader(file)
        for lines in reader:
            usernamelist.append(lines[1])
        file.close()
        if username in usernamelist:
            print("A user has been found.")
            return [user for user in listofusers if user.username == username]
        else:
            print("There was no user found.")
            return None
    except FileNotFoundError:
        saveaccounts()
            
    
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

def saveoneaccount(username):
    useraccount = [account for account in listofusers if account.username == username]
    if len(useraccount) == 0:
        print("Sorry, the account details could not be saved.")
    else:
        with open("accounttext.txt", "a") as writer:
            writer.write(useraccount)
        print("The account details were saved.")
    

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
                username = input("What is the username of the account for which you would like to search?n#\n").strip()
                searchforaccount(username)
            case "delete":
                userid = input("What is the user id of the account that you would like to delete?\n").strip()
                deleteaccount(userid)
            case "save all":
                saveaccounts()
            case "save one":
                username = input("What is the username of the account that you would like to save to a text file?\n").strip()
                saveoneaccount(username)
        attempts = 3
        contchoice = ""
        while contchoice not in ["y", "n"] and attempts > 0:
            contchoice = input("Would you like to continue running the program? y/n\n")
            attempts -= 1
            
        

if __name__ == "__main__":
    main()