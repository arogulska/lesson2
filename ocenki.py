school_results = [
                    {'school_class': '1a', 'scores': [3,4,4,5,2]}, 
                    {'school_class': '1b', 'scores': [1,1,3,5,1]}, 
                    {'school_class': '1c', 'scores': [3,5,4,4,1]},
                    {'school_class': '2a', 'scores': [4,4,5,3,4]},
                    {'school_class': '2b', 'scores': [2,3,3,2,5]},
                    {'school_class': '2c', 'scores': [5,4,3,2,1]}
                    ]

def scoring():
    
  for dictionary in school_results:
      print (
        "For class " + dictionary['school_class'] + " the average is: " + 
        str((sum(dictionary['scores'])/len(dictionary['scores'])))
        )



def school_avg():

  scores_lists = [dictionary['scores'] for dictionary in school_results]
  scores_total = sum((sum(scores) for scores in scores_lists))
  len_total = sum(len(dictionary['scores']) for dictionary in school_results)
 
  print ("The school average is: " + str(scores_total / len_total))
    

  
scoring()

school_avg()
