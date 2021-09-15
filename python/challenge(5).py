import time
clock_name = 'clock'
clock_info=time.get_clock_info(clock_name)
print("information on '%s': " %clock_name)
print(clock_info)

clock_name = 'pref_counter'
clock_info = time.get_clock_info(clock_name)
print("information on '%s': " %clock_name)
print(clock_info)

clock_name= 'monotonic'
clock_info = time.get_clock_info(clock_name)
print("information on '%s': " %clock_name)
print(clock_info)

clock_name='process_time'
clock_info = time.get_clock_info(clock_name)
print("information on '%s': " %clock_name)