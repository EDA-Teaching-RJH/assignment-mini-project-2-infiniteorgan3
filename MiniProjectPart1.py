# This file contains the classes that are used within the main program.
class UserAccount:
    def __init__(self, username, password, email, listofotherusers = None, userid = None):
        # If the username is not entered or the username is not unique, being entered by another user.
        if not username or self.checkusername(username, listofotherusers) == "":
            raise ValueError("The username is already taken or is invalid.")
        self.username = username
        # If the user's email is not entered with the definition of the object.
        if not email:
            raise ValueError("The email is invalid.")
        self.email = email
        # If the user's password is not enterd properly with the definition of the object in the program.
        if not password:
            raise ValueError("The password entered is invalid.")
        self.password = password
        # This is used if the user account is being created for the first time in the program, with the user ID being required to be unique.
        if userid == None:
            self.userid = self.assignuserid(listofotherusers)
        # This is only used when the user is changing the type of their account, and so their unique user id has already been assigned.
        else:
            self.userid = userid
            
    # This is defined for when an individual user account is being saved to a text file, which is the same for the overridden method for the StudentAccount child class.
    def __str__(self):
        return f"UserID: {self.userid}: Username: {self.username}, Email: {self.email}, Password: {self.password}"
    
    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if not username:
            raise ValueError("The username is already taken or is invalid.")
        self._username = username
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        if not password:
            raise ValueError("The password entered is invalid.")
        self._password = password
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if not email:
            raise ValueError("The email is invalid.")
        self._email = email
        
    @property
    def userid(self):
        return self._userid
    
    @userid.setter
    def userid(self, userid):
        self._userid = userid
        
    
    # The user ID is iterated, and the value of the current user ID is based on the the length of the total list of users (initialised at the start of the main program).
    def assignuserid(self, listofusers):
        matches = [0]
        i = 0
        # If a user ID is taken, then iterate the user ID checked until one that is not taken by another user is found, which is then assigned to the user.
        while len(matches) != 0:
            uid = len(listofusers) + i
            matches = [account for account in listofusers if account.userid == uid]
            i += 1
        return uid
    
    # The username is checked to see if it is unique, returning an empty string so that a ValueError can be raised if the username is identical to one of another user.
    def checkusername(self, username, listofusers):
        matches = [account for account in listofusers if account.username == username]
        if len(matches) != 0:
            return ""
        return username
    
# The StudentAccount is a child class of the UserAccount due to the fact that it would be a subset of the general user account and would be saved differently if saved in the main program.
class StudentAccount(UserAccount):
    def __init__(self, username, password, email, coursesubject, listofotherusers = None, userid = None):
        super().__init__(username, password, email, listofotherusers, userid)
        # The unique attribute of the course is defined and validated, only being able to take a value from the below list, otherwise raising a ValueError.
        if coursesubject not in ["BIO","CHEM","EEE","ECE","MECHE","BIOE","PHY","PSYCH","SOCIO","ENGL","MATHS","HIST","GEO","MED","VET"]:
            raise ValueError("The course subject is invalid.")
        self.coursesubject = coursesubject
    
    
    def __str__(self):
        return f"UserID: {self.userid}: Username: {self.username}, Email: {self.email}, Password: {self.password}, Subject: {self.coursesubject}"
    
    # The getter and setter for the course subject as the data for the course can be changed within the main program as an option.
    @property
    def coursesubject(self):
        return self._coursesubject

    @coursesubject.setter
    def coursesubject(self, coursesubject):
        if coursesubject not in ["BIO","CHEM","EEE","ECE","MECHE","BIOE","PHY","PSYCH","SOCIO","ENGL","MATHS","HIST","GEO","MED","VET"]:
            raise ValueError("The course subject is invalid.")
        self._coursesubject = coursesubject
