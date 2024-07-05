import random
import string
import os
a = 1
while a == 1:
    os.system("cls")
    hand = int(input("Enter 1 for custom pass word \n Enter 2 from defult pasword\t"))
    if hand == 1:
        a = 2
    elif hand == 2:
        a = 2 
    else:
        print("Enter the corect number")
os.system("cls")
tol_pass = int(input("Tedad char ra moshaxas konid :"))
os.system("cls")
if a == 1:
    number = str(input("Enter the number:"))
    os.system("cls")
    chaar = str(input("Enter the char wana :"))
    os.system("cls")
    spe_char = str(input("Enter the special char:"))
    os.system("cls")
    master_pass = number + chaar + spe_char
    pasvord = ''
    for i in range(tol_pass):
        pasvord += ''.join(random.choice(master_pass))
    print(pasvord)
elif a == 2:
    special_characters = string.punctuation
    digits = string.digits
    letters = string.ascii_letters
    pass_characters = letters + digits + special_characters
    password = ''
    for i in range(tol_pass):
        password += ''.join(random.choice(pass_characters))
    print(password)
    