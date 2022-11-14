print ("Welcome to the Quiz Game")

playing = input("Do you want to play this Game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Start the Game \n")
score = 0


answer = input("Capital of India? \n")
if answer.lower() == "new delhi":
    print("Your Answer is Correct.\n")
    score += 1
else:
    print("Opps, Your Answer is Incorrect.\n")


answer = input("National Animal of India? \n")
if answer.lower() == "tiger":
    print("Your Answer is Correct.\n")
    score += 1
else:
    print("Opps, Your Answer is Incorrect.\n")


answer = input("What does RAM stands for? \n")
if answer.lower() == "random access memory":
    print("Your Answer is Correct.\n")
    score += 1
else:
    print("Opps, Your Answer is Incorrect.\n")


answer = input("What does ROM stands for? \n")
if answer.lower() == "read only memory":
    print("Your Answer is Correct.\n")
    score += 1
else:
    print("Opps, Your Answer is Incorrect.\n")


answer = input("What does CPU stands for? \n")
if answer.lower() == "central processing unit":
    print("Your Answer is Correct.\n")
    score += 1
else:
    print("Opps, Your Answer is Incorrect.\n")


answer = input("What does UPS stands for? \n")
if answer.lower() == "uninterruptible power supply":
    print("Your Answer is Correct.\n")
    score += 1
else:
    print("Opps, Your Answer is Incorrect.\n")

print("You Total Score is " + str(score))
print("Thanks for playing :)")