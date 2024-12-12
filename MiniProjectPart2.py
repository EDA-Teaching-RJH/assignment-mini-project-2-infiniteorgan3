import MiniProjectPart1
import re
import csv

# This is the account that can be used to create an account to be added to the list of users and saved to a CSV file.
def createaccount(listofusers):
    # This is for the validation of the username input, as there are two possible reasons for the username to be considered as invalid.
    reasonsforinvalid = []
    # This limits the number of times an invalid input can be made until the program moves past it and raises the error when creating the account at the end of the process of creation.
    attempts = 3
    username = ""
    # This is validating the username inputs by calling a function to validate the username using a regular expression.  
    while type(validateusername(username)) == list and attempts > 0:
        reasonsforinvalid = validateusername(username)
        if attempts != 3:
            for i in reasonsforinvalid:
                print(i)
        username = input("Please enter a username for the account:\n").strip()
        attempts -= 1
    reasonsforinvalid.clear()
    # Ensuring that the account creation is unsucessful if an invalid value is entered.
    if attempts == 0:
        username = ""
        reasonsforinvalid.append("Invalid username.")
    password = ""
    attempts = 3
    # This is validating the inputs by calling a function to validate the password using a regular expression.
    while validatepassword(password) == None and attempts > 0:
        password = input("Please enter the password for the account:\n")
        attempts -= 1
    if attempts == 0:
        password = ""
        reasonsforinvalid.append("Invalid password.")
    email = ""
    attempts = 3
    # This is validating the inputs by calling a function to validate the email using a regular expression.  
    while validateemail(email) == None and attempts > 0:
        email = input("Please enter your email:\n")
        attempts -= 1
    if attempts == 0:
        email = ""
        reasonsforinvalid.append("Invalid email.")
    typeaccount = None
    isstudent = False
    attempts = 3
    # This determines whether the attempted account being created will be a student account or a general user account but the validation.
    while typeaccount not in ["student", "unaffiliated"] and attempts > 0:
        typeaccount =  input("Are you a student or unaffiliated with the university? (student/unaffiliated)\n").lower().strip()
        attempts -= 1
    # If the category is invalid and has not been entered by the time in which the loop is exited, the user account creation is not attempted and instead, the function is exited prematurely.
    if attempts == 0:
        print("You did not enter a valid type of account.")
        return None
    # The type of account being created is determined, and if the account type being created is a student account, then the course being studied is inputted and converted to uppercase prior to the creation of the account.
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
        # If the account could not be created, then the reasons for the account being unable to be created will be listed before the function ends. 
        print("The user account could not be created, please try again.\nThe reasons for the creation of the account failing were:")
        for i in reasonsforinvalid:
            print(i)
    else:
        # If the new user is successfully created, then it is added to the list of all users and the data is saved to the CSV file containing the data of all of the accounts so that the data cannot be lost if the program closes without the user saving all of the accounts.
        listofusers.append(newuser)
        saveaccounts(listofusers)

# This saves all of the account information to a CSV file, to be read from when initialising the value of the list when the program is run.
def saveaccounts(listofusers):
    # The headers are created before the file is created or overwritten
    dataentries = ["UserID","Username","Email","Password", "Is Student", "Course"]
    # The rows is a list of all of the lists of the attributes of all of the user accounts.
    rows= []
    for i in listofusers:
        # Determining whether the account is a student account, with the differences in data being processed and added to the rows to be written to the csv file.
        if isinstance(i, MiniProjectPart1.StudentAccount) == True:
            rows.append([i.userid, i.username, i.email, i.password, "Yes", i.coursesubject])
        else:
            rows.append([i.userid, i.username, i.email, i.password, "No", "N/A"])
    
    # Writing all of the data of the list of users to the CSV file, overwriting any pre-existing data
    with open("allaccountinfo.csv","w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataentries)
        csvwriter.writerows(rows)

    print("All of the accounts' information has been saved.")

# This will remove the account from the list of the users, and overwrite the CSV file storing all data about the accounts, thus removing the user from the file.
def deleteaccount(userid, listofusers):
    # The user ID can only be checked if the user ID is a valid user ID, and so is an integer.
    try:
        userid = int(userid)
    except ValueError:
        print("The ID you have entered is invalid.")
    else:
        # Find the user associated with the user ID.
        attemptedresultreturn = [account for account in listofusers if account.userid == userid]
        # The deletion can only be completed if the account associated with the user ID exists, and so it is checked.
        if attemptedresultreturn != []:
            # The user is removed from the list and the CSV file is overwritten, and saved.
            listofusers.remove(attemptedresultreturn)
            saveaccounts()
        else:
            print("The user could not be found.")

# The account will be searched for the unique username and all of them are extracted from the file, if the username being searched is in the list of all of the usernames then the user information will be returned.           
def searchforaccount(username, listofusers):
    usernamelist = []
    try:
        file = open("allaccountinfo.csv", "r")
        reader = csv.reader(file)
        # Creating a list of all of the usernames of the accounts that have been created.
        for lines in reader:
            usernamelist.append(lines[1])
        file.close()
        # Checking whether the username is in the list of all of the usernames, and print an appropriate message and the user information if found.
        if username in usernamelist:
            print("A user has been found.")
            print([user for user in listofusers if user.username == username])
        else:
            print("There was no user found.")
    # If the CSV file does not exist, then save the list of users so that the CSV file is created.
    except FileNotFoundError:
        print("No users currently exist, creating the file for all user information.")
        saveaccounts()

# Validating the email passed to the function using a regular expression to find whether the email fits into the specified format.
def validateemail(email):
    regexpattern = re.compile(r"^([A-Za-z0-9]+[_\.\-])*[A-Za-z0-9]+@\w+(\.([A-Za-z]{2,}))+")
    if re.fullmatch(regexpattern, email) == None:
        print("This email has an invalid format.")
        # Return None so that the while loop in the account creation function can easily be maintained.
        return None
    else:
        return email
       
# Validating the username passed to this function using a regular expression to determine whether the length and characters used in the username are appropriate.
def validateusername(username):
    # Returning the list of reasons that the validation failed, to be printed in the account creating function to specify what the user must change so that the username will be valid.
    reasons = []
    regexpattern = r"^(([\w\.\-]){5,})$"
    if re.search(regexpattern, username) == None:
        if len(username) < 5:
            reasons.append("The username is too short and must be at least 5 characters.")
        if re.search(r"(.)*[^\w\.\-](.)*", username):
            reasons.append("The username contains invalid characters. The valid characters are alphanumeric characters, dots, underscores and dashes.")
        return reasons
    else:
        return username

# Validating the password passed to this function using a regular expression to determine whether the length and characters used in the password are appropriate.
def validatepassword(password):
    if re.search(r"[\w\.+*=#()&!?%\-]{8,}", password) == None:
        if len(password) < 8:
            print("The password is invalid because it is too short and must be at least 8 characters.")
        if re.search(r"(.)*[^\w\.+*=#()&!?%\-](.)*", password):
            print("The password is invalid because it contains invalid characters. The valid characters are alphanumeric characters, full stops, pluses, astrices, hashes, dashes, exclamation marks, question marks, percentage signs, ampersands, equals signs and brackets.")
        # Return None so that the while loop in the account creation function can easily be maintained.
        return None
    else:
        return password

# Saving a string of the information stored for a specific account in a text file, appending to it when the user decides to add to the file.
def saveoneaccount(username, listofusers):
    # Checking if the account exists from the username input.
    useraccount = [account for account in listofusers if account.username == username]
    if len(useraccount) == 0:
        print("Sorry, the account details could not be saved.")
    else:
        with open("accounttext.txt", "a") as writer:
            # Checking if the user account information is in the text file, so that duplicate information is not stored.
            with open("accounttext.txt", "r") as reader:
                lines = reader.readlines()
            # So that all of the lines can be checked for the data trying to be stored, the data will only be written after all lines have been checked.
            for line in lines:
                if line == str(useraccount):
                    print("The account information is already saved to the file.")
                    # Ending the function if duplicate information is found so that no data is written.
                    return None
                writer.write(useraccount)
        print("The account details were saved.")

# Editing the course of an account that is a student account and saving the new user data to the CSV file.
def editcourse(userid, listofusers):
    # The user ID can only be checked if the user ID is a valid user ID, and so is an integer.
    try:
        userid = int(userid)
    except ValueError:
        print("The ID you have entered is invalid.")
    else:
        # Find the user associated with the user ID.
        useraccount = (account for account in listofusers if account.userid == userid)
        # The course of the student account can only be edited if the account exists, and so its existence must be verified.
        if useraccount == None:
            print("The account was not found, please try again.")
            return False
        
        # Checking whether the account is a Student or not, as the process can only proceed if the account is a student account.
        if isinstance(useraccount, MiniProjectPart1.StudentAccount):
            # Validating the course to which they would like to change, while limiting the number of attempt they can use to do so. 
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
                # If no valid course is entered, then exit the function with a message and do not save the CSV file.
            if attempts == 0:
                print("Please try again, your request could not be completed.")
            else:
                print("The course was changed successfully.")
                saveaccounts()
        else:
            print("The account with which you are attempting to perform this operation is not a student account, please try again or change their account type.")

# Allowing the user account to be reinstated as either a general user or a student account depending on the type of account they had prior.
def changeaccounttype(userid, listofusers):
    # The user ID can only be checked if the user ID is a valid user ID, and so is an integer.
    try:
        userid = int(userid)
    except ValueError:
        print("The ID you have entered is invalid.")
    else:
        # The state of the account can only be edited if the account exists, and so its existence must be verified.
        useraccount = (account for account in listofusers if account.userid == userid)
        if useraccount == None:
            print("The user account being searched does not exist.")
        else:
            # Reinstating a student account as a general user account, only requring the removal of the course variable from the student account as well as removing the old student account version of their account.
            if isinstance(useraccount, MiniProjectPart1.StudentAccount) == True:
                listofusers.remove(useraccount)
                listofusers.append(MiniProjectPart1.UserAccount(useraccount.username, useraccount.password, useraccount.email, listofusers, useraccount.userid))
            # Reinstating a user account as a student account requires the input and validation of the course, which if unsuccessful in the number of allotted attempts, the account will remain unchanged.
            else:
                validcourse = False
                attempts = 3
                while validcourse == False and attempts > 0:
                    courseinput = input("Please enter the course that the user is entering.").upper()
                # Ensuring that the course is valid to be added as a parameter of the new student account.
                    try:
                        listofusers.append(MiniProjectPart1.StudentAccount(useraccount.username, useraccount.password, useraccount.email, courseinput, useraccount.userid))
                        validcourse == True
                        # Removing the old user account if the new student account is instated.
                        listofusers.remove(useraccount)
                    except ValueError:
                        print("The course that you have entered is not valid, please try again.")
                    attempts -= 1
                if attempts == 0:
                    print("Please try again, your request could not be completed.")
            # Saving the states of the accounts irrespective of the request failing or succeeding.
            saveaccounts()

# Initialising the list of users so that all of the user information can be accessed from starting the program without potentially causing issues like duplicating user information or losing it unintentionally.
def initialiselistofaccounts():
    # Initialising the list of user accounts from the CSV file in which they are saved.
    listofusers = []
    try:
        with open("allaccountinfo.csv", "r") as filereader:
            reader = csv.reader(filereader)
            # Ensuring that the headers are not included and attempted to be processed as users.
            next(reader)
        for row in reader:
            # Processing the values stored in the files and adding them to the list of users as either student or general user accounts by creating objects with the same values.
            if row[4] == "Yes":
                listofusers.append(MiniProjectPart1.StudentAccount(row[1], row[3], row[2], row[5], int(row[0])))
            else:
                listofusers.append(MiniProjectPart1.UserAccount(row[1], row[3], row[2], int(row[0])))
    except FileNotFoundError:
        # If the file does not exist then it should be created, although it will be an empty file initally.
        saveaccounts(listofusers)
        pass
    # Returns an empty list if the file does not exist or a list of values if it already exists.
    return listofusers              


def main():
    listofusers = initialiselistofaccounts()
    # Ensure that the user can perform multiple operations within the program before exiting it.
    continuation = True
    while continuation == True:
        validchoices = ["create","search","delete","save all", "save one", "edit course", "change type"]
        print("Welcome to the program to save and create user accounts, the options for utilising the program are:\n1. Creating a New Account.(create)\n2. Searching for a user account.(search)\n3. Deleting a user account.(delete)\n4. Saving all of the accounts to a file.(save all)\n5. Saving the information of one account.(save one)\n6. Edit the course of a student account.(edit course)\n7.Change the type of user account.(change type)")
        inputchoice = ""
        # Validating the choice of the user, where if it is not validated, the program will be exited due to a choice not being selected.
        attempts = 3
        while inputchoice not in validchoices and attempts > 0:
            inputchoice = input("What would you like to do?").lower().strip()
        if attempts == 0:
            print("No request was made and so the program will close.")
            break
        # Running a suitable function, and taking any prior inputs necessary for its operation, depending on the choice made by the user.
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
        # Asking the user whether they would like to continue running the program and validating their response.
        attempts = 3
        contchoice = ""
        while contchoice not in ["y", "n"] and attempts > 0:
            contchoice = input("Would you like to continue running the program? y/n\n").strip().lower()
            attempts -= 1
        # If no valid choice is made, then the choice to continue is automatically set to "n".
        if attempts == 0:
            contchoice = "n"
        if contchoice == "n":
            print("Thank you for using the program.")
            continuation = False
        
if __name__ == "__main__":
    main()