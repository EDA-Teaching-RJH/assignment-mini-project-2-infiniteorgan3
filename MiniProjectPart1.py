import re
import random
# account system:
class UserAccount:
    def __init__(self, username, password, email, userid, listofotherusers = None):
        if not username or self.checkusername(username, listofotherusers):
            raise ValueError("The username is already taken.")
        self.username = username
        self.email = email
        if not password:
            raise ValueError("The password entered is not valid.")
        self.password = password
        self.userid = self.assignuserid(listofotherusers)
        
    def assignuserid(self, listofusers):
        uid = 0
        while uid == 0 or uid in vars(listofusers)["userid"]:
            uid = random.randint(1, 65356)
    
    def checkusername(username, listofusers):
        if username in vars(listofusers)["username"]:
            return ""
        return username
    
    