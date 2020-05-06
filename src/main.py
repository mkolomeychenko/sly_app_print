import time

print("app: start")

for i in range(5):
	time.sleep(1)
	print("app_log: ", i)


print("app: finish")