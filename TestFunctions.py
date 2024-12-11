import MiniProjectPart2

def testvalidatingpassword():
    assert MiniProjectPart2.validateemail("ee@kent.ac.uk") == "ee@kent.ac.uk"
    assert MiniProjectPart2.validateemail("test@example.com")
    assert MiniProjectPart2.validateemail("t_@@kent.com")
    assert MiniProjectPart2.validateemail("t.tkent.c")
    assert MiniProjectPart2.validateemail("t%j@example.com")
    assert MiniProjectPart2.validateemail("example@kent.ac.uk")