import MiniProjectPart2

def testvalidatingpassword():
    MiniProjectPart2.validateemail("ee@kent.ac.uk")
    MiniProjectPart2.validateemail("test@example.com")
    MiniProjectPart2.validateemail("t_@@kent.com")
    MiniProjectPart2.validateemail("t.tkent.c")