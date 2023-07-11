# import the date class

from datetime import date
from datetime import datetime

# calling the today
# function of date class

datetime.today()

# date object of today's date
today = datetime.today()

type(today)



today_date = date.today()

today_date


type(today_date)


today_date.month

today_date.year

today_date.day

christmas = date(today_date.year, 12, 25)
christmas

if christmas != today_date:
    print("Sorry there are still " + str((christmas - today_date).days) + " until Christmas!")
else:
    print("Yay it's Christmas!")