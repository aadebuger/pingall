# -*- coding: utf-8 -*-
'''
Created on 2014年1月27日

@author: aadebuger
'''
import multiprocessing
from subprocess import Popen
import pexpect
def pingip(ipaddr):
    playcommand="ping"
    p= Popen([playcommand,"-c","3",ipaddr])
    p.wait()    
def pexpectpingip(ipaddr):
    playcommand="ping"
    foo = pexpect.spawn('ping -c 1 %s'%(ipaddr))  
    foo.expect (pexpect.EOF) 
    print 'foo.before=',foo.before

    return foo.before
 
def pingall():
    retv = []
    for i in range(190,256):
        newip = "192.168.60.%d"%(i)
        print newip
        try:
            ret=pexpectpingip(newip)
            if ret.find("100.0% packet loss")==-1:
                retv.append(newip)
        except Exception,e:
            print 'e=',e 

    print 'retv=',retv
if __name__ == '__main__':
    pexpectpingip("192.168.60.1")
    pingall()