# your code goes here!
import time

def countdown(num):
    while num >= 0:
        if num == 0:
            print("HAPPY NEW YEAR!")
        else:
            print(f"{num} SECOND(S)!")
        num -= 1
    pass

def countdown_with_sleep(num):
    while num >= 0:
        if num == 0:
            print("HAPPY NEW YEAR!")
        else:
            print(f"{num} SECOND(S)!")
        time.sleep(1)
        num -= 1
    pass