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



    size =input("Please enter size for that pizza")







