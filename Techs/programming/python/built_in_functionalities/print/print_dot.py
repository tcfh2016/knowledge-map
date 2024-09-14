import time

start = time.time()
time.sleep(5)
end = time.time()

print("time wait: {diff:.2f}".format(diff=end-start))
