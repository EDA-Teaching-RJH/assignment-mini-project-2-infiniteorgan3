import random
# account system:
class UserAccount:
    def __init__(self, username, password, email, listofotherusers = None):
        if not username or self.checkusername(username, listofotherusers) == "":
            raise ValueError("The username is already taken or is invalid.")
        self.username = username
        if not email:
            raise ValueError("The email is invalid.")
        self.email = email
        if not password:
            raise ValueError("The password entered is invalid.")
        self.password = password
        self.userid = self.assignuserid(listofotherusers)
    
    def __str__(self):
        return f"UserID: {self.userid}: Username: {self.username}, Email: {self.email}, Password: {self.password}"
    
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
    def __init__(self, username, password, email, coursesubject):
        UserAccount.__init__(self, username, password, email, listofotherusers=None)
        if coursesubject not in ["BIO","CHEM","EEE","ECE","MECHE","BIOE","PHY","PSYCH","SOCIO","ENGL","MATHS","HIST","GEO","MED","VET"]:
            raise ValueError("The course subject is invalid.")
        self.coursesubject = coursesubject
    
    def __str__(self):
        return f"UserID: {self.userid}: Username: {self.username}, Email: {self.email}, Password: {self.password}, Subject: {self.coursesubject}"
    
    @coursesubject.setter
    def coursesubject(self, coursesubject):
        if coursesubject not in ["BIO","CHEM","EEE","ECE","MECHE","BIOE","PHY","PSYCH","SOCIO","ENGL","MATHS","HIST","GEO","MED","VET"]:
            raise ValueError("The course subject is invalid.")
        self._coursesubject = coursesubject

    @property
    def coursesubject(self):
        return self._coursesubject
