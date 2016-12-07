import threading
from time import sleep, ctime

class MyThread(threading.Thread):
    
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
        self.func = func
        
    def getResult(self):
        return self.res
    
    def run(self):
        print 'starting ', self.name, 'at:', ctime()
        self.res = self.func(*self.args)
        print self.name, 'finished at:', ctime()