# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 09:36:19 2016

@author: yang
"""

import threading
from myThread import MyThread
from time import sleep, ctime

def fib(x):
    sleep(0.05)
    if x < 2:
        return 1
    return fib(x-2) + fib(x-1)

def fac(x):
    sleep(0.05)
    if x < 2:
        return 1
    return (x * fac(x-1))

def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x + sum(x-1))

funcs = [fib, fac, sum]
n = 12

def main():
    nfuncs = range(len(funcs))
    print('*** SIGNLE THRED')
    for i in nfuncs:
        print 'starting', funcs[i].__name__, 'st:', ctime()
        print funcs[i](n)
        print funcs[i].__name__, 'finished at:', ctime()
    
    print '\n *** multiple threads'
    
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)
    
    for i in nfuncs:
        threads[i].start()
        
    for i in nfuncs:
        threads[i].join()
        print threads[i].getResult()
        
    print 'all DONE'
    
if __name__ == '__main__':
    main()