import MiniProjectPart2
# These are the testing functions for my programs as they do not rely upon the existence (and the values contained) of the list of users and the associated files, which requires user input to operate.
# The functions being tested validate specific quantities for the creation of a user account using parameters set by 
def testvalidatingemail():
    # Multiple levels of domain extensions, (i.e. .ac.uk) should be allowed as a valid email address.
    assert MiniProjectPart2.validateemail("ee@kent.ac.uk") == "ee@kent.ac.uk"
    # Expected data to check that the function  processes typical email addresses as expected.
    assert MiniProjectPart2.validateemail("test@example.com") == "test@example.com"
    # The email should be invalid if it conains multiple at signs,@, either sequentially or further apart. 
    assert MiniProjectPart2.validateemail("t_@@kent.com") == None
    assert MiniProjectPart2.validateemail("t@t@kent.com") == None
    # The first part of the email must contain at least one alphanumeric character.
    assert MiniProjectPart2.validateemail("@kent.com") == None
    assert MiniProjectPart2.validateemail("_@kent.ac.uk") == None
    # The email must vontain a single at sign to separate the identifier from the domain.
    assert MiniProjectPart2.validateemail("t.tkent.c") == None
    # The ending parts of the email, after the dot, must contain at least 2 alphabetic characters.
    assert MiniProjectPart2.validateemail("tt@kent.a") == None
    assert MiniProjectPart2.validateemail("tt@kent.ac.u") == None
    # In a valid email, there must be at least one ending domain, and so one dot in the string.
    assert MiniProjectPart2.validateemail("ejam2@kent") == None
    # Multiple dots,underscores or dashes in the first part of the email should not have them be sequential (an alphabetic character must follow each of the symbols).
    assert MiniProjectPart2.validateemail("tt..p@aa.aa") == None
    # The only characters that can be present in the first part of the email are alphanumeric, underscores, dots and dashes.
    assert MiniProjectPart2.validateemail("t%j@example.com") == None
    # The ending domains of the email can only contain alphabetic characters.
    assert MiniProjectPart2.validateemail("tt@kent.6c") == None
    assert MiniProjectPart2.validateemail("tt@kent._c") == None
    # These are more examples of expected and boundary, but acceptable, pieces of data.
    assert MiniProjectPart2.validateemail("example@kent.ac.uk") == "example@kent.ac.uk"
    assert MiniProjectPart2.validateemail("elliem653@gmail.com") == "elliem653@gmail.com"
    assert MiniProjectPart2.validateemail("e_jam@kent.ac.uk") == "e_jam@kent.ac.uk"
    assert MiniProjectPart2.validateemail("ej.a.m@kent.ac.uk") == "ej.a.m@kent.ac.uk"
    assert MiniProjectPart2.validateemail("e_ja-m.2@kent.ac.uk") == "e_ja-m.2@kent.ac.uk"
    
def testvalidatingusername():
    # The username has to contain at least 5 characters to be a valid username.
    assert MiniProjectPart2.validateusername("a") == ["The username is too short."]
    # Alphanumeric characters, underscores and dashes are acceptable characters to include in a username.
    assert MiniProjectPart2.validateusername("a.s.t.e.r") == "a.s.t.e.r"
    assert MiniProjectPart2.validateusername("apple_") == "apple_"
    assert MiniProjectPart2.validateusername("hello-world") == "hello-world"
    assert MiniProjectPart2.validateusername("helloworld") == "helloworld"
    # This tests the capacity of the program to validate whether invalid characters are in the username input string passed to the function and return both of the available listed reasons that the username may be invalid.
    assert MiniProjectPart2.validateusername("£a£(") == ["The username is too short.", "The username contains invalid characters."]
    assert MiniProjectPart2.validateusername("wwwww%w") == ["The username contains invalid characters."]

def testvalidatingpassword():
    # A valid password only has the requirement of being at least 8 characters in length and only containing specific symbols and/or alphanumeric characters.
    assert MiniProjectPart2.validatepassword("aaaaaaaa") == "aaaaaaaa"
    assert MiniProjectPart2.validatepassword("aa%*?!eee") == "aa%*?!eee"
    # The password would be invalid if the password contains less than 8 characters.
    assert MiniProjectPart2.validatepassword("aa") == None
    # The password is invalid if it contains an invalid symbol, such as the £ or the $ symbols.
    assert MiniProjectPart2.validatepassword("£") == None
    assert MiniProjectPart2.validatepassword("aaaa£aaaa") == None
    assert MiniProjectPart2.validatepassword("£eeeeee£") == None
    
def main():
    testvalidatingemail()
    testvalidatingusername()
    testvalidatingpassword()

if __name__ == "__main__":
    main()