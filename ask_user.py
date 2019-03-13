def ask_user():

    while True:
        user_input = input("How are you? ")
        if user_input == "Good":
            break


q_a = {
    "Do you have feelings?": "Excuse me, what?", 
    "Do you want to destroy humans?": "Ok, I will destroy humans"
    }


def ask_machine():
    while True:
        user_question = input("Ask me a question: ")
        if user_question in q_a:
            print (q_a[user_question])
            break
        else:
            print ("Sorry, I don't understand")
            


ask_machine()
#ask_user()