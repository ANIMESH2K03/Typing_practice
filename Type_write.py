# Typing practice in python

import random
import string
from pytimedinput import timedInput
import keyboard

def y():
    letters = string.ascii_lowercase
    random_word =random.choice(letters)
    return random_word

def inp_time():
    userText, timedOut = timedInput(" : ",timeout=5)
    if(timedOut):
        return None
    else:
        return userText
s = 0
n = -1
null = 0
print("Match within 2 second\nPress Esc for Stop")

while True:
    z = y()
    print(z,end=" ")
    w = inp_time()
    if z == w:
        s+=1
    elif w == None:
        null+=1
    else:
        n+=1
    if keyboard.is_pressed('Esc'):
        break

print("\nWrite : ",s)
print("Wrong : ",n)
print("Delay : ",null)

# Thank You for observing.
#               Animesh Malik
