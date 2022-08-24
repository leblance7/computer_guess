#guess the computer's number
import random
print('Im comtemplating a number')
computer_choice=random.randint(1,100)
print('DEBUG',computer_choice)
print('take a guess ')
while True:
    input_value = input("Please input a number")
    y = int(input_value)
    if computer_choice > y:
        print('too low')
    if computer_choice < y:
        print('too high')
    if computer_choice == y:
        print ('good job!')
        break
    


    





