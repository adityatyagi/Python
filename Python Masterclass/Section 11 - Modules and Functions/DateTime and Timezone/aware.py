"""
Aware v/s Naive
"""
import time
import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

# --------------------- AWARE TIME ----------------------------------
print("This is the NAIVE local time: {} ".format(local_time))
print("This is the NAIVE utc time: {} ".format(utc_time))

# converting naive to aware objects
aware_localtime = pytz.utc.localize(utc_time).astimezone()
aware_utctime = pytz.utc.localize(utc_time)

print("Aware local time {}, timezone {}".format(aware_localtime, aware_localtime.tzinfo)) 
# aware_localtime.tzinfo -> gives the Indian Standard Time
# aware_localtime gives the localtime + offset

print("Aware UTC time {} in timezone {}".format(aware_utctime, aware_utctime.tzinfo))




print()
print('-----Example of converting date & time to timestamp----------')
#----------------- EXAMPLE --------------------------------
gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0) # 2015-10-25 01:30:00
print(gap_time)
print(gap_time.timestamp()) # timestamp gives the seconds since epoch till the date passed to it

print()
print('-----Example of converting timestamp to date and time----------')
s = 1445716800
t = s + (60*60) # adding one hour for DST

# using the timezone of great britain
gb = pytz.timezone('GB') 
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb) #fromtimestamp(s) - can be used, but better to use the utcfromtimestamp, because we always work with utc, and only display the result in local time to the user
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print('{} seconds since the epoch is {}'.format(s, dt1))
print('{} seconds since the epoch is {}'.format(t, dt2))