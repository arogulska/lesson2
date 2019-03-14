q_a = {
    "Do you have feelings?": "Excuse me, what?", 
    "Do you want to destroy humans?": "Ok, I will destroy humans"
    }


def ask_machine(dictionary, command, other):
              
    while True:

        try:

            user_question = input(command)
            if user_question in dictionary:
                print (dictionary[user_question])
                
            else:
                print (other)
                
        
        except KeyboardInterrupt:
            print ("\n" + "Bye!")
            break
        


ask_machine(q_a, "Ask me a question: ", "Sorry, I don't understand")