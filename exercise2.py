def string_f():

    string1 = "python is"
    string2 = "a snake"

    if type(string1) != str or type(string2) != str:
        print (0)

    if string1 == string2:
        print (1)
    
    if string1 != string2 and len(string1) > len(string2):
        print (2)

    if string1 != string2 and string2 == "learn":
        print (3)

    

string_f()
