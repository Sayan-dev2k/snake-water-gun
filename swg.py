import random
i=0
you=0
comp=0
while(i<10):
    a=input("Enter your chioce(s/w/g):")
    lst=["snake","water","gun"]
    b=random.choice(lst)
    print("computer's choice:",b)
    if(a=="snake"):
        if(b=="water"):
            you=you+1
        elif(b=="gun"):
            comp=comp+1
        else:
            print("both 0")
    elif(a=="water"):
        if(b=="gun"):
            you=you+1
        elif(b=="snake"):
            comp=comp+1
        else:
            print("both 0")
    elif(a=="gun"):
        if(b=="snake"):
            you=you+1
        elif(b=="water"):
            comp=comp+1
        else:
            print("both 0")
    i=i+1
print("Total points...")
print("You:",you)
print("computer:",comp)
if(you>comp):
    print("you are the winner with total points",you)
else:
    print("Computer is the winner with total points",comp)  