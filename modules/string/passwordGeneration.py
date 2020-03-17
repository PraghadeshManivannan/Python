import random
import string
from string import Template

def password(leng , choice):
    if choice == 1:
        letters = string.ascii_lowercase
    elif choice == 2:
        letters = string.ascii_uppercase
    elif choice == 3:
        letters = string.ascii_letters
    elif choice == 4:
        letters = string.ascii_letters + string.digits
    elif choice == 5:
        letters = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(letters) for i in range(leng))

t = Template('Random Password is $pwd')

#weak password in lowercase
pwd = password(10,1)
s = t.substitute(pwd = pwd )
print(s)

#weak password in uppercase
pwd = password(10,2)
s = t.substitute(pwd = pwd )
print(s)

#weak password in lowercase and uppercase
pwd = password(10,3)
s = t.substitute(pwd = pwd )
print(s)

#medium password with lowercase, uppercase and digits
pwd = password(10,4)
s = t.substitute(pwd = pwd )
print(s)

#strong password with lowercase, uppercase, digits and puntuations
pwd = password(10,5)
s = t.substitute(pwd = pwd )
print(s)