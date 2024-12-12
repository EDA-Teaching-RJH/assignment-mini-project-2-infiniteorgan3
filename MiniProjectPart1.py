import random
# This file contains the classes that are used within the main program.
class UserAccount:
    def __init__(self, username, password, email, listofotherusers = None, userid = None):
        if not username or self.checkusername(username, listofotherusers) == "":
            raise ValueError("The username is already taken or is invalid.")
        self.username = username
        if not email:
            raise ValueError("The email is invalid.")
        self.email = email
        if not password:
            raise ValueError("The password entered is invalid.")
        self.password = password
        if userid == None:
            self.userid = self.assignuserid(listofotherusers)
        # This is only used when the user is changing the type of their account, and so their unique user id has already been assigned.
        else:
            self.userid = userid
            
    
    def __str__(self):
        return f"UserID: {self.userid}: Username: {self.username}, Email: {self.email}, Password: {self.password}"
    
    @property
    def userid(self):
        return self._userid
    
    @property
    def password(self):
        return self._password
    
    @property
    def email(self):
        return self._email
    
    @property
    def username(self):
        return self._username
    
    def assignuserid(self, listofusers):
        uid = 0
        matches = []
        while uid == 0 or len(matches) != 0:
            uid = random.randint(1, 65356)
            matches = [user for user in listofusers if user.userid == uid]
    
    def checkusername(username, listofusers):
        matches = [account for account in listofusers if account.username == username]
        if len(matches) != 0:
            return ""
        return username
    
class StudentAccount(UserAccount):
    def __init__(self, username, password, email, coursesubject, listofusers = None, userid = None):
        super().__init__(self, username, password, email, listofotherusers = None, userid = None)
        if coursesubject not in ["BIO","CHEM","EEE","ECE","MECHE","BIOE","PHY","PSYCH","SOCIO","ENGL","MATHS","HIST","GEO","MED","VET"]:
            raise ValueError("The course subject is invalid.")
        self.coursesubject = coursesubject
    
    
    def __str__(self):
        return f"UserID: {self.userid}: Username: {self.username}, Email: {self.email}, Password: {self.password}, Subject: {self.coursesubject}"
    

    @property
    def coursesubject(self):
        return self._coursesubject
    
    @coursesubject.setter
    def coursesubject(self, coursesubject):
        if coursesubject not in ["BIO","CHEM","EEE","ECE","MECHE","BIOE","PHY","PSYCH","SOCIO","ENGL","MATHS","HIST","GEO","MED","VET"]:
            raise ValueError("The course subject is invalid.")
        self._coursesubject = coursesubject
