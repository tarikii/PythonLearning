import time

# print(time.ctime(0))

# print(time.time())

# print(time.ctime(time.time()))

# time_object = time.localtime()
# time_object = time.gmtime()
# print(time_object)
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# time_string = "01 July, 2023"
# time.strptime(time_string, "%d %B %Y")


time_tuple = (2023, 7, 1, 16, 5, 0, 5, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

