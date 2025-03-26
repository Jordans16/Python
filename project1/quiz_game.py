print("welcome to my quiz")

playing = input(" Do you want to play? ")

if playing != "yes":
    quit()

print("Good!!! let us start")
score = 0

#the .lower() is for making sur the answer of the player is convert to lower
answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect")


answer = input("what does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect")


answer = input("what does RAM stand for? ")
if answer.lower() == "ramdom access memory":
    print("correct")
    score += 1
else:
    print("Incorrect")

print("you got " + str(score) + " questions correct")