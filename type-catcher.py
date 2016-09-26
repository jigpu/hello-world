def my_function(blah):
    if type(blah) == int:
        print "That's an integer!"
    elif type(blah) == float:
        print "That's a float!"
    elif type(blah) == str:
        print "That's a string!"
    else:
        print "I have no idea what that is."

blah = raw_input("Type something")
my_function(blah)
