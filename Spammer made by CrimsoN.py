#CrimsoN
#Spammer

import pyautogui as auto
import time

i=10

print("Spammer made by CrimsoN")
print("")

while i>1:
    spam=input("What would you like to spam?: ")
    counter=int(input("How many times would you like to spam? Min = 1, max = 100: "))
    print("*You will have 5 seconds before the spam begins*")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    for i in range (0,counter):
        auto.write(spam)
        auto.press("enter")
        
        
        

