# Typing practice in python

import random
import string

def y():
    letters = string.ascii_lowercase
    random_word = ''.join(random.choice(letters) for i in range(1))
    return random_word

n=0
o=0
while True:
    z = y()
    print(z,end=" ")
    inp2 = str(input())
    if inp2 == "end" or inp2 == "stop":
        break
    else:
        if inp2 == z:
            n+=1
        else:
            o+=1

print("Total Wrong :",o)
print("Score : ",n)

# Thank You for observing.
#               Animesh Malik.