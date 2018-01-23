import random
from secrets import randbelow
import time

def is_number(possible_number):
    try:
        int(possible_number)
        return True
    except ValueError:
        return False

print("Welcome to E-Lottery")
print(" version 2.57 © KSE Studios")
print("Please enter your six lottery numbers")
num1 =input()
num2 = input()
num3 = input
num4 = input()
num5 = input()
num6 =input()



print("Thank you for entering. These are the winning numbers:")
time.sleep(5)



lottery_numbers = randbelow((20)), randbelow((20)), randbelow((20)), randbelow((20)), randbelow((20)), randbelow((20))
print(lottery_numbers)


if lottery_numbers != num1 and num2 and num3 and num4 and num5 and num6:
    print("Sorry, you did not win this time.")
    print("Try again next month.")
elif lottery_numbers == num1 and num2 and num3 and num4 and num5 and num6:
    print("Congragulations! You just won the jackpot")


