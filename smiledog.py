me = input ("Rock (r), Paper (p), or Scissors (s)?")

import random
chosen = random.randint(1, 3)

if me == ("r"):
    print ("You did rock") 
if me == ("p"):
    print ("You did paper") 
if me == ("s"):
    print ("You did scissors") 

if chosen==1:
    print("and I did rock")
elif chosen==2:
    print("and I did paper")
else:
    print("and I did scissors")

if chosen==1 and me == ("r"):
    print ("Tie")
elif chosen==2 and me == ("r"):
    print ("Covered: I win.")
elif chosen==3 and me == ("r"):
    print ("Crushed: You win.")
elif chosen==1 and me == ("p"):
    print ("Covered: You win.")
elif chosen==2 and me == ("p"):
    print ("Tie")
elif chosen==3 and me == ("p"):
    print ("Shredded: I win.")
elif chosen==1 and me == ("s"):
    print ("Crushed: I win.")
elif chosen==2 and me == ("s"):
    print ("Shredded: You win.")
elif chosen==3 and me == ("s"):
    print ("Tie")
else:
    print ("Put in a real option next time.")
