# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 08:58:03 2016

@author: yang
"""

import threading
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
    
def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))
    
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
        
    for i in nloops:
        threads[i].start()
        
    for i in nloops:
        threads[i].join() #等待线程结束
        
    print('all DONE at:', ctime())

words = ['cat', 'window', 'defenestrate']
word = words[:]
for w in (word):
    if len(w) > 6:
        words.insert(0, w)
print(words)      
#if __name__ == '__main__':
    #main()
    
    