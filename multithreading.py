from  time import  sleep
from threading import *

class Hi(Thread):

    def run(self):
        for i in range(5):
            print("Hiiii")
            sleep(2)


class Hello(Thread):
     def run(self):
         for i in range(5):
             print("Heloooo")
             sleep(2)

t1=Hi()
t2 = Hello()

t1.start()
sleep(1)
t2.start()

t1.join()
t2.join()
print("Byeeeeeeeeee")

