from datetime import time,date,timedelta

time_1 = time()
print('Time_1: {}'.format(time_1))

time_2 = time(hour=10,minute=45,second=47,microsecond=123458)
print('Time_2: {}'.format(time_2))

today = date.today()
outbreak = date(2002,11,10)
daysSinceOutbreak = today - outbreak
print(daysSinceOutbreak)

tomorrow = today + timedelta(seconds=86400)
print(tomorrow)