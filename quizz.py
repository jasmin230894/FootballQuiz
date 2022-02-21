print("welcome to my football quiz")

playing=input("Do you want to play ??? ")
if playing.lower()!="yes":
    quit()
print("Okay, let's play :)")
score=0

answer=input("Who is the top scorer of all time in the champions league? ")
if answer.lower()=="cristiano ronaldo":
    print("correct!!!")
    score+=1
else:
    print("incorrect :(")

answer=input("Who win World Cup in 2014? ")
if answer.lower()=="germany":
    print("correct!!!")
    score+=1
else:
    print("incorrect :(")

answer=input("Which player never won Champions league ? Zlatan Ibrahimovic, Samuel Eto or Thiery Henry ")
if answer.lower()=="zlatan ibrahimovic":
    print("correct!!!")
    score+=1
else:
    print("incorrect :(")

answer=input("How many goals Lionel Messi scored in 2012? ")
if answer=="91":
    print("correct!!!")
    score+=1
else:
    print("incorrect :(")


print("You got " +str(score)+ " questions correct")
print("You got " +str((score/4)*100)+ "%")
