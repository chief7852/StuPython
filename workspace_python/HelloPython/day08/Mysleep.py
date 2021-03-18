import time
from threading import Thread
def work() :
    for i in range(10):
        print("안녕")
        time.sleep(1)
START, END = 0, 100000000
result = list()

th1 = Thread(target=work)
th2 = Thread(target=work)
th3 = Thread(target=work)
th4 = Thread(target=work)
th5 = Thread(target=work)
th6 = Thread(target=work)

th1.start()
time.sleep(0.3)
th2.start()
time.sleep(0.3)
th3.start()
time.sleep(0.3)
th4.start()
time.sleep(0.3)
th5.start()
th1.join()
th2.join()
th3.join()
th4.join()
th5.join()