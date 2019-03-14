def ask_user():

    while True:
        user_input = input("How are you? ")
        if user_input == "Good":
            break


q_a = {
    "Do you have feelings?": "Excuse me, what?", 
    "Do you want to destroy humans?": "Ok, I will destroy humans"
    }


def ask_machine(dictionary, command, other):
    while True:
        user_question = input(command)
        if user_question in dictionary:
            print (dictionary[user_question])
            break
        else:
            print (other)
            


ask_machine(q_a, "Ask me a question: ", "Sorry, I don't understand")
#ask_user()