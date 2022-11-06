import time, datetime
from random import randint

for i in range (1,45):
    print(" ")

s = ""
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
year = int(year)+1

for i in range(1,1000):
    count = randint(1,100)
    while (count > 0):
        s += " "
        count -= 1
    if (i%10==0):
            print(s + "Happy New Year {}".format(year))
    else:
        print(s + "*")
    s = ""
    time.sleep(0.1)
