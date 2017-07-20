import time
from time import process_time as my_timer # first time is the module, second is the fucntion
import random

input('Enter to start: ')
waitRandomTime = random.randint(1,6) # will return a random number between 1 and 6

# the program will stop its execution for a PARTICUALR period of time
# and after that time, the program will resume executing
time.sleep(waitRandomTime)

startTime = my_timer()

input("Press Enter to stop")

endTime = my_timer()

print("Started at: " + time.strftime("%X", time.localtime(startTime))) # %X	Locale’s appropriate time representation.
print("Ended at: " + time.strftime("%X", time.localtime(endTime)))
print("Your reaction time was {} seconds".format(endTime - startTime))

