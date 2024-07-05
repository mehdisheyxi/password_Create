# فراخوانی ماژول های موردنیاز
import random
import string
# فراخوانی ثابت های موردنیاز
print
special_characters = string.punctuation
digits = string.digits
letters = string.ascii_letters
# قرار دادن همه ثابت ها در یک متغیر
pass_characters = letters + digits + special_characters
# تعیین طول متغیر توسط کاربر
pass_length = int (input ("Enter the number lenght::\t"))
# متغیر حاوی پسورد ساخته شده
password = ''
# حلقه سازنده پسورد
for i in range(pass_length):
    password += ''.join(random.choice(pass_characters))
# نمایش پسورد ساخته شده به کاربر
print(password)
print(digits)
print(special_characters)
print(letters)
print(type(digits))
print(type(special_characters))
print(type(letters))