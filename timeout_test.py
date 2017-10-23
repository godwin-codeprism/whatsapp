import time 
import threading 

time_passed = 0
max_time = 5

def setTimeout():
    global time_passed
    global max_time
    while time_passed < max_time:
        time.sleep(1)
        time_passed += 1
        print(time_passed)
    else:
        print("Time up")

t1 = threading.Thread(target=setTimeout)
t1.start()

while time_passed < max_time:
    print("time_passed")
else:
    print("Good bye")