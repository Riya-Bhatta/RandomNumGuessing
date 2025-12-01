import datetime
import time
name = input("welcome, enter your name :")
presentHour =datetime.datetime.now().hour
if 5<= presentHour <= 12:
    print("Good morning ", name)
    
elif 12 <= presentHour <16:
        print("Good morning ", name)
  
elif 16<= presentHour <20:
        print("Good evening ", name)
    
else:
    print("Good night", name)
    print("Hello ! Welcome to your ChatBot")
    print("you can ask me basic question , Type 'bye' to exit from the bot")
    
communication={
        "hello" : " Hi ,welcome to the AI Chat Bot",
        "how are you" : "I am fine" ,
        "who are you" : " I am smart Chat Bot",
        
        "happy" : "Glad to hear it ",
        "motivate me" : " you are doing good coding .keep doing",
    }
def communicationOfBot(userQuestion):
    userQuestion =userQuestion.lower()
    for eachkey in communication: 
        if eachkey in userQuestion:
            return communication[eachkey] 
            return " i am not able to tell that yet. I will learn it very soon"
while True:
    userInput = input("please ask your question:")
    reply =  communicationOfBot(userInput)
    print("Bot Response :",reply)
    if "bye"  in userInput.lower():
        break 
    
    
    
    