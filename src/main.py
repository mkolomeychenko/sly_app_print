import time
import os

print("app: start,  PID = {}".format(os.getpid()))

i = 0
while True:
	time.sleep(5)
	print("app_log: ", i)
	i += 1


print("app: finish")