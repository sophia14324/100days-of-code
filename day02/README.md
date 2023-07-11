# Python DateTime module

The Datetime module comes built into Python, so there is no need to install it externally. 

The DateTime module is categorized into 6 main classes – 

1. date – An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. Its attributes are year, month, and day.

2. time – An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. Its attributes are hour, minute, second, microsecond, and tzinfo.

3. datetime – Its a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo.

4. timedelta – A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.

5. tzinfo – It provides time zone information objects.

6. timezone – A class that implements the tzinfo abstract base class as a fixed offset from the UTC (New in version 3.2).

## How the code works
The year, month, and date of the current day is got from the date object using the year, month and date attribute of the date class, then calculates how many days Christmas is to the specified date.