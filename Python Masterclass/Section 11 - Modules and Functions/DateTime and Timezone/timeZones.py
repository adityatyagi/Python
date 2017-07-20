import time
import datetime
import pytz

print("The epoch time at this system starts at: " + time.strftime('%c', time.gmtime(0)))

print('the current timezone is {} with the offset value of {}'.format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print('Daylight saving time is in effect for this system')
    print('The DST timezone is '+ time.tzname[1])


print('Local time is '+ time.strftime('%Y-%m-%d %I-%M-%S', time.localtime())) # %I is for 12-Hour clock
print('UTC time is '+ time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())) # %H is for 24-Hour clock

# https://docs.python.org/3/library/datetime.html#module-datetime
'''
Aware and Naive objects are two kinds of date and time objects

Aware objects are aware of the timezone offsets while the naive ones are not

date objects are naive and datetime objects can be aware
while using date objects, ignore timezonesa and DST
'''

print(datetime.datetime.today()) # Return the current local date. 
print(datetime.datetime.now()) # Return the current local date and time. If optional argument tz is None or not specified, this is like today()
# If tz is not None, it must be an instance of a tzinfo subclass, and the current date and time are converted to tz’s time zone

print(datetime.datetime.utcnow())
# Return the current UTC date and time, with tzinfo None. This is like now(), but returns the current UTC date and time, as a naive datetime object.
# An aware current UTC datetime can be obtained by calling datetime.now(timezone.utc).


# ------------------ DISPLAY TIME IN A PARTICULAR COUNTRY ---------------------
country = 'Europe/Moscow'
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display) # tz_to_display is a tz_info object that .now() takes as a parameter
print("the time in {} is {}".format(country, local_time))
utc_time = datetime.datetime.utcnow()
print("the UTC time in {} is {}".format(country, utc_time))


#------------------ Dispaly all the countires timezones ----------------------
for i in pytz.all_timezones:
    print(i)




#------------------ Dispaly all the countires timezones with COUNTRY CODES ----------------------
for i in sorted(pytz.country_names):
    print(i +': '+ pytz.country_names[i])


for i in sorted(pytz.country_names):
    print('{}: {} ----> {}'.format(i, pytz.country_names[i], pytz.country_timezones.get(i))) 
 
# .get(i) gives "none" if there is no value for certain item
# pytz.country_timezones[i] would give an error on BV -> will give KeyError: 'BV'

print()
print('-------------------------------------------------------')

# ALTERNATIVE WAY TO WRITE CODE
# check if the key contains a value and then proceed
for i in sorted(pytz.country_names):
    print('{}: {}'.format(i, pytz.country_names[i]), end=': ')
    if i in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[i]):
            zone_to_display = pytz.timezone(zone)
            localtime = datetime.datetime.now(tz=zone_to_display)
            print('\t\t{}: {}'.format(zone, localtime))
        
    else:
        print("No time zone defined") 



print()
print('$'*80)

