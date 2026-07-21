import random

print("What is my nagic number (1 to 100) ?")
mynumber = random.randint(1,100)
ntries = 1
yourhuess = -1
while ntries <7 and ___________________________ :
    msg = str(ntries) + ">>"
    if (ntries == 6) :
        ____________________
    yourguess = int(input(msg))
    if ____________________ :
        print("--> too high")
    ____________________ :
        print(--> too low)
    ntries += 1

if ____________________ :
        print("yes! it's" mynumber)
else :
     print("Sorry! my number is", mynumber)