# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 09:52:57 2016

@author: yang
"""

from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen as uopen

REGEX = compile('#([\d,]+) in BOoks ')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '738478329439': 'Python Web Development with Python',
    '32983492': 'python fundamentals',
}

def getRanking(isbn):
    page  = uopen('%s%s' %(AMZN, isbn))
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]

def _showRanking(isbn):
    print '-%r ranked %s' % (ISBNs[isbn], getRanking(isbn))
    
def main():
    print 'at', ctime(), 'on Amazon...'
    for isbn in ISBNs:
        _showRanking(isbn)
        
if __name__ == '__main__':
    main()
