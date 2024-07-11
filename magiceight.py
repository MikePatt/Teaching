# Import the modules
import random

answers = ["It is certain","Outlook good","You may rely on it","Ask again later","Concentrate and ask again", 
"Reply hazy, try again","My reply is no","My sources say no","Ask again soon"]

while True:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    if question == "":
        print("GoodBye!")
        break
    
    print(random.choice(answers))
    
    
