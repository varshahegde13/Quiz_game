print("Welcome to my computer quiz !!!")

playing = input("Do you want to play the game?: ")
score = 0

if playing.lower()!= "yes":
    quit()
print("Okay!! Let's play :)")

answer = input("What does RAM stand for ?")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input(" What is the full form of GPT in Chat GPT? ")
if answer.lower() == " generative pre-trained transformer":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What is the speed of the computer measured it?")
if answer.lower() == "gigahertz":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("You got"   +  str(score)  +  "questions correct !")
print("You got"  +   str((score / 4)* 100 ) +  "questions correct!! ")
