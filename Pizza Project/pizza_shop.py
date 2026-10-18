from order import *

order ={}

print("-" * 20)
username = input("Please Enter username to sign in...")


while True:
    prompt =input("Do you wish to order a pizza  y/n    Yes|No").lower()


    if prompt == "yes" or prompt == "y":
        nickname =input("Please enter a nickname for that pizza")

        if nickname not in order:
            order[username]= "nickname"
        else:
            print(f"{nickname} is already been used.Please choose another")



    size =input("Please enter size for that pizza")
    toppings = []
    while True:
        choice= input("Enter topping you want for you pizza or Press x to finish Order")
        if choice == "X":
            break
        toppings.append(choice)











