import random
from secrets import randbelow
import time
from random import sample



print("Welcome to E-Lottery")
print(" version 2.57 © KSE Studios")
print("Please enter your six lottery numbers 1- 20.")



    
while True:
    try:
        num1 = int(input())
        while 1> num1 >20:
            print("Please input number again:")
            num1 =int(input())
        num2 = int(input())
        while 1> num2 > 20:
            print("Please input number again:")
            num2 =int(input())
        num3 = int(input())
        while 1> num3 >20:
            print("Please input number again:")
            num3 =int(input())
        num4 = int(input())
        while 1> num4 >20:
            print("Please input number again:")
            num4 = int(input())
        num5 =int(input())
        while 1> num5 > 20:
            print("Please input number again:")
            num5 =int(input())
        num6 = int(input())
        while 1> num6 >20:
            print("Please input number again:")
            num6 = int(input())

        break
    except ValueError:
        print(" No....")
        time.sleep(2)
        print("ENTER A VALID NUMBER!")
        


print("Thank you for entering. These are the winning numbers:")
time.sleep(5)



lottery_numbers = randbelow((20)), randbelow((20)), randbelow((20)), randbelow((20)), randbelow((20)), randbelow((20))
print(lottery_numbers)

if lottery_numbers != guesses:
    print("Sorry, you did not win this time.")
    print("Try again next month.")
elif lottery_numbers == guesses:
    print("Congragulations! You just won the jackpot")
    

