import time
import os

print("PID:{}".format(os.getpid()))
print("app: start")

i = 0
while True:
	time.sleep(5)
	print("app_log: ", i)
	i += 1


print("app: finish")