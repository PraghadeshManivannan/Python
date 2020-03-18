from datetime import date,datetime

today = {}

print("The date is",date.today())
print("The time is",datetime.now())

print("Year:",datetime.now().year)
today['Year'] = datetime.now().year

print("Day:",datetime.now().day)
today['Day'] = datetime.now().day

print("Month:",datetime.now().month)
today['Month'] = datetime.now().month

print("Hour:",datetime.now().hour)
today['Hour'] = datetime.now().hour

print("Minute:",datetime.now().minute)
today['Minute'] = datetime.now().minute

print("Second:",datetime.now().second)
today['Second'] = datetime.now().second

print("Micro second:",datetime.now().microsecond)
today['Micro second'] = datetime.now().microsecond

#strftime() takes one parameter to specify the format of the output string

#Month
print('Month in full form:',datetime.now().strftime('%B'))#Month in full form
print('Month in small form:',datetime.now().strftime('%b'))#Month in small form
today['Month in full form'] = datetime.now().strftime('%B')

#Day
print('Day in full form:',datetime.now().strftime('%A'))#Day in full form
print('Day in short form:',datetime.now().strftime('%a'))#Day in short form
today['Day in full form'] = datetime.now().strftime('%A')

#Weekday as number
print('Day of the week:',datetime.now().strftime('%w'))#Day as number
today['Day of the week'] = datetime.now().strftime('%w')

#date of the month
print('Date of the month:',datetime.now().strftime('%d'))#date of the month

#month as number
print('Month as a number:',datetime.now().strftime('%m'))#month as a number

#week of the year
print('Week of the year:',datetime.now().strftime('%W'))#week of the year
today['Week of the year'] = datetime.now().strftime('%W')

#using replace() we can change the attributes
print('This day in next year:',datetime.now().replace(year = datetime.now().year - 1).strftime('%A')) 

print(today)