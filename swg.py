import random
i=0
while(i<10):
    a=input("Enter your chioce(s/w/g):")
    lst=["snake","water","gun"]
    b=random.choice(lst)
    print("computer's choice:",b)
    if(a=="snake"):
        if(b=="water"):
            print("you:1 comp:0")
        elif(b=="gun"):
            print("you:0 comp:1")
        else:
            print("both 0")
    elif(a=="water"):
        if(b=="gun"):
            print("you:1 comp:0")
        elif(b=="snake"):
            print("you 0 comp:1")
        else:
            print("both 0")
    elif(a=="gun"):
        if(b=="snake"):
            print("you:1 comp:0")
        elif(b=="water"):
            print("you:0 comp:1")
        else:
            print("both 0")
    i=i+1

print("The winner is...")
print("******atmanirbhar bano babu***")    