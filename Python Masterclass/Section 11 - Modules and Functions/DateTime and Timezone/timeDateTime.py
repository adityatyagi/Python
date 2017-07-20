''' 
There are two main problems with date and time;
1. localization
2. daylight savings

Localization: time of a particular place and also the format in which it isi represented there

Daylight Savings Time (DST): involves moving the clock forward in spring, resulting in
everyone getting up 1 hour earlier, so that everyone can take advantage of the extra daylight
as the sun rises up 1 hour early in the morning. This doesn't happens everywhere.
The clock is the put back 1 hour in autumn. 


For scientific and computer realted stuff, we work in Coordinated Universal Time (UTC) or Zulu Time

Dates and Times are usually stored in UTC, along with the offset to represent the number of hours ahead/behind
of UTC and a flag to indicate if DST applies to that particluar location or not 

Python provides with 3 modules to deal with date and time
1. time         (elapsed time)
2. datetime     (date and time)
3. calender

https://docs.python.org/3/library/time.html

'''

import time

# 0 specifies the start of the epoch
# gmtime() always works in UTC
# generates a named tuple
# converts number of seconds to struct_time(), which is a named tuple
print(time.gmtime(0))

# provides the local time
# generates a named tuple
# converts number of seconds to struct_time(), which is a named tuple
print(time.localtime(time.time()))
print(time.localtime()) # same result as above

# provides the number of seconds elapsed since the start of the epoch, i.e 
# number of seconds for 1/1/1970 to 20/7/2017
print(time.time())



# -------------------ACCESSING TUPLES------------------------------------------

time_here = time.localtime() # beacuse .localtime() returns a tuple
print(time_here)

# time_here is a tuple now and thus can be accessed in that way
print('Year: ', time_here[0])
print('Month: ', time_here[1])
print('Day: ', time_here[2])
#--------OR-------------------
print('Year: ', time_here.tm_year)
print('Month: ', time_here.tm_mon)
print('Day: ', time_here.tm_mday)
print('Hours: ', time_here.tm_hour)
print('Minutes: ', time_here.tm_min)
print('Seconds: ', time_here.tm_sec)




# --------------------------------------------------------------

'''
perf_counter: it gives accurate measure of the elapsed time, but it doesnt return a real time value
it is the most precise clock, it is used to benchmark code
it has high resolution on some systems and therefore it makes sense to use that in comparsion to
monotonic
though the differnce between the two is very low
best to measure elapsed time


monotonic: the clock can't go backwards, so we cannot make any adjustments dure to the DST, as well as
it will not affect the computer's clock


process_time: the time used by CPU to execute the program 


NOTE: PERF_COUNTER AND PROCESS_TIME are MONOTONIC

https://www.python.org/dev/peps/pep-0418/
'''

