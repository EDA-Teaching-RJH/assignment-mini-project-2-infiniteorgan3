import MiniProjectPart1
import re
import csv

def createaccount(listofusers):
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
        saveaccounts(listofusers)
    
def saveaccounts(listofusers):
    dataentries = ["UserID","Username","Email","Password", "Is Student", "Course"]
    rows= []
    for i in listofusers:
        if isinstance(i, MiniProjectPart1.StudentAccount) == True:
            rows.append([i.userid, i.username, i.email, i.password, "Yes", i.coursesubject])
        else:
            rows.append([i.userid, i.username, i.email, i.password, "No", "N/A"])
    
    with open("allaccountinfo.csv","w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataentries)
        csvwriter.writerows(rows)

    print("All of the accounts' information has been saved.")

def deleteaccount(userid, listofusers):
    try:
        userid = int(userid)
    except ValueError:
        print("The ID you have entered is invalid.")
    else:
        attemptedresultreturn = [account for account in listofusers if account.userid == userid]
        if attemptedresultreturn != []:
            listofusers.remove(attemptedresultreturn)
            saveaccounts()
                
def searchforaccount(username, listofusers):
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
    regexpattern = r"^[A-Za-z0-9]+[\.-_]?[A-Za-z0-9]+@\w+([.]\w{2, })+$"
    if re.search(regexpattern, email) == None:
        print("This email has an invalid format.")
        return None
    else:
        return email
        
def validateusername(username):
    reasons = []
    regexpattern = r"^(([\w\.]){5, })$"
    if re.search(regexpattern, username) == None:
        if len(username) < 5:
            reasons.append("The username is too short.")
        if re.search(r"(.)*[^\w.-](.)*", username):
            reasons.append("The username contains invalid characters.")
        return reasons
    else:
        return username

def validatepassword(password):
    if re.search(r"[\w.+-*=#()&!?%]{8, }", password) == None:
        if len(password) < 8:
            print("The password is invalid because it is too short.")
        if re.search(r"(.)*[^\w\.+-*=#()&!?%](.)*", password):
            print("The password is invalid because it contains invalid characters.")
        return None
    else:
        return password

def saveoneaccount(username, listofusers):
    useraccount = [account for account in listofusers if account.username == username]
    if len(useraccount) == 0:
        print("Sorry, the account details could not be saved.")
    else:
        with open("accounttext.txt", "a") as writer:
            writer.write(useraccount)
        print("The account details were saved.")


def editcourse(userid, listofusers):
    try:
        userid = int(userid)
    except ValueError:
        print("The ID you have entered is invalid.")
    else:
        useraccount = (account for account in listofusers if account.userid == userid)
        if useraccount == None:
            print("The account was not found, please try again.")
            return False
        
        if isinstance(useraccount, MiniProjectPart1.StudentAccount):
            validcourse = False
            attempts = 3
            while validcourse == False and attempts > 0:
                courseinput = input("Please enter the course that the user is being changed to.").upper()
                try:
                    useraccount.coursesubject = courseinput
                    validcourse == True
                except ValueError:
                    print("The course that you have entered is not valid, please try again.")
                    attempts -= 1
            if attempts == 0:
                print("Please try again, your request could not be completed.")
            print("The course was changed successfully.")
            saveaccounts()
        else:
            print("The account with which you are attempting to perform this operation is not a student account, please try again or change their account type.")

def changeaccounttype(userid, listofusers):
    try:
        userid = int(userid)
    except ValueError:
        print("The ID you have entered is invalid.")
    else:
        useraccount = (account for account in listofusers if account.userid == userid)
        if useraccount == None:
            print("The user account being searched does not exist.")
        else:
            if isinstance(useraccount, MiniProjectPart1.StudentAccount) == True:
                listofusers.append(MiniProjectPart1.UserAccount(useraccount.username, useraccount.password, useraccount.email, listofusers, useraccount.userid))
            else:
                validcourse = False
                attempts = 3
                while validcourse == False and attempts > 0:
                    courseinput = input("Please enter the course that the user is entering.").upper()
                try:
                    listofusers.append(MiniProjectPart1.StudentAccount(useraccount.username, useraccount.password, useraccount.email, courseinput, useraccount.userid))
                    validcourse == True
                except ValueError:
                    print("The course that you have entered is not valid, please try again.")
                    attempts -= 1
                if attempts == 0:
                    print("Please try again, your request could not be completed.")
            saveaccounts()

def initialiselistofaccounts():
    # Initialising the list of user accounts from the CSV file in which they are saved.
    listofusers = []
    try:
        with open("allaccountinfo.csv", "r") as filereader:
            reader = csv.reader(filereader)
            headers = next(reader)
        for row in reader:
            if row[4] == "Yes":
                listofusers.append(MiniProjectPart1.StudentAccount(row[1], row[3], row[2], row[5], int(row[0])))
            else:
                listofusers.append(MiniProjectPart1.UserAccount(row[1], row[3], row[2], int(row[0])))
    except FileNotFoundError:
        pass
    return listofusers              

def main():
    listofusers = initialiselistofaccounts()
    continuation = True
    while continuation == True:
        validchoices = ["create","search","delete","save all", "save one", "edit course", "change type"]
        print("Welcome to the program to save and create user accounts, the options for utilising the program are:\n1. Creating a New Account.\n2. Searching for a user account.\n3. Deleting a user account.\n4. Saving all of the accounts to a file.\n5. Saving the information of one account.\n6. Edit the course of a student account.\n7.Change the type of user account.")
        inputchoice = ""
        attempts = 3
        while inputchoice not in validchoices and attempts > 0:
            inputchoice = input("What would you like to do?").lower().strip()
        if attempts == 0:
            print("No request was made and so the program will close.")
            break
        match inputchoice:
            case "create":
                createaccount(listofusers)
            case "search":
                username = input("What is the username of the account for which you would like to search?n#\n").strip()
                searchforaccount(username, listofusers)
            case "delete":
                userid = input("What is the user id of the account that you would like to delete?\n").strip()
                deleteaccount(userid, listofusers)
            case "save all":
                saveaccounts()
            case "save one":
                username = input("What is the username of the account that you would like to save to a text file?\n").strip()
                saveoneaccount(username, listofusers)
            case "edit course":
                userid = input("What is the user id of the account that you would like to edit?\n").strip()
                editcourse(userid, listofusers)
            case "change type":
                userid = input("What is the user id of the account that you would like to change the type of?\n").strip()
                changeaccounttype(userid, listofusers)
        attempts = 3
        contchoice = ""
        while contchoice not in ["y", "n"] and attempts > 0:
            contchoice = input("Would you like to continue running the program? y/n\n").strip().lower()
            attempts -= 1
        if attempts == 0:
            contchoice = "n"
        if contchoice == "n":
            print("Thank you for using the program.")
            continuation = False
        
if __name__ == "__main__":
    main()