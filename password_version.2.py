import random
import string
import os
def pas_coustom():
    tool = int(input("Enter the tedad char pass ra :\t"))
    adad = str(input("Enter adad haye ramz ra :\t"))
    matn = str(input("char haye daxl ramz ra vared konid "))
    shekl = str(input("Enter the ashkal pass ra:\t"))
    passaz = adad + matn + shekl 
    password = ''
    for i in range(tool):
        password+= ''.join(random.choice(passaz))
    print(f"this is pass-----------\n{password}\nthis is pass^^^^^^^^^^")
    ss = input("Press any key...")
        
def pas_defult():
    tool = int(input("Enter the tedad char pass ra :\t"))
    special = string.punctuation
    digit = string.digits
    matnesh = string.ascii_letters
    passaz = special + digit + matnesh
    password = ''
    for i in range(tool):
        password += ''.join(random.choice(passaz))
    print(f"this is pass-----------\n{password}\nthis is pass^^^^^^^^^^")
    ss = input("Press any key...")

while(True):
    os.system("cls")
    print("WELCOME TO CREATE PASSWORD APP\n ")
    a = int((input("press 1 for defult\npress 2 for coustom::")))
    if a == 1:
        pas_defult()
    elif a== 2:
        pas_coustom()
    else:
        print("adad Eshteba vared kardid!!")
        ms = input("press key to returnt")