# options = ['load data', 'export data', 'analyze & predict']
#
# UserchoiceStr = True
#
# while UserchoiceStr:
#     print(options)
#     UserchoiceStr = input("Please enter no of item from list above: ")
#     if UserchoiceStr.isdecimal():
#         UserChoice = int(UserchoiceStr)
#         if UserChoice in range(len(options)):
#             print(UserChoice, " " ,options[UserChoice])
#         else:
#             print("Your choice out of range!!!!")
#
#
#     else:
#         print("Your choice is not Integer")

import sys

options = ['load data', 'export data', 'analyze & predict']

choice = 'x'

def DisplayOptions(lista):
    for i in range(len(lista)):
        print(i+1, " - ",lista[i])
    user_choice = input("Select option above or press enter to exit: ")
    return user_choice


while choice:
    choice = DisplayOptions(options)
    if choice:
        try:
            choice_num = int(choice)
            if choice_num > 0 and choice_num <= len(options):
                print("Index from options list: ",choice_num, "Element from options list: ", options[choice_num-1],",", options)
            else:
                print("Your choice out of range!!!!")
        except:
            print("Number should be entered - index of options list!!", sys.exc_info()[0])
    else:
        print("Koniec działania programu")








