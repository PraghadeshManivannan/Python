import string
from string import Template

#string constants

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.whitespace)
print(string.punctuation)


#Template

t = Template('Hi this is $name')
s = t.substitute(name='Jarvis')
print(s)