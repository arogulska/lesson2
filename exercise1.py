age = int(input("How old are you? "))

def what_to_do():

    if age <= 6:
        print ("you should go to kindergarten")

    elif 6 < age <= 19:
        print ("you should go to school")

    elif 19 < age <= 24:
        print ("you should go to university")

    elif 24 < age <= 65:
        print ("work work work!")

what_to_do()
