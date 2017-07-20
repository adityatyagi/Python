# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.

import time

print('Time: \t\t\t', time.get_clock_info('time'))
print('Monotonic Time: \t', time.get_clock_info('monotonic'))
print('Performance Counter: \t', time.get_clock_info('perf_counter'))
print('Process time: \t\t', time.get_clock_info('process_time'))

'''
The result has the following attributes:

adjustable: True if the clock can be changed automatically (e.g. by a NTP daemon) or manually by the system administrator, False otherwise
implementation: The name of the underlying C function used to get the clock value
monotonic: True if the clock cannot go backward, False otherwise
resolution: The resolution of the clock in seconds (float)

'''