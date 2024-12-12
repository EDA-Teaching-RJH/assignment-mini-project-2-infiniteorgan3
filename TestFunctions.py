import MiniProjectPart2

def testvalidatingemail():
    assert MiniProjectPart2.validateemail("ee@kent.ac.uk") == "ee@kent.ac.uk"
    assert MiniProjectPart2.validateemail("test@example.com") == "test@example.com"
    assert MiniProjectPart2.validateemail("t_@@kent.com") == None
    assert MiniProjectPart2.validateemail("t.tkent.c") == None
    assert MiniProjectPart2.validateemail("t%j@example.com") == None
    assert MiniProjectPart2.validateemail("example@kent.ac.uk") == "example@kent.ac.uk"
    assert MiniProjectPart2.validateemail("elliem653@gmail.com") == "elliem653@gmail.com"
    
def testvalidatingusername():
    assert MiniProjectPart2.validateusername("a") == ["The username is too short."]
    #assert MiniProjectPart2.validateusername("a.s.t.e.r") == "a.s.t.e.r"
    assert MiniProjectPart2.validateusername("apple_") == "apple_"
    assert MiniProjectPart2.validateusername("hello-world") == "hello-world"
    assert MiniProjectPart2.validateusername("£a£(") == ["The username is too short.", "The username contains invalid characters."]
    assert MiniProjectPart2.validateusername("wwwww%w") == ["The username contains invalid characters."]

def testvalidatingpassword():
    assert MiniProjectPart2.validatepassword("aaaaaaaa") == "aaaaaaaa"
    assert MiniProjectPart2.validatepassword("aa%*?!eee") == "aa%*?!eee"
    assert MiniProjectPart2.validatepassword("aa") == None
    assert MiniProjectPart2.validatepassword("£") == None
    assert MiniProjectPart2.validatepassword("aaaa£aaaa") == None
    assert MiniProjectPart2.validatepassword("£eeeeee£") == None
    
def main():
    #testvalidatingemail()
    testvalidatingusername()
    testvalidatingpassword()

if __name__ == "__main__":
    main()