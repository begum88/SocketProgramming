#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:08:23 2016

@author: begumpasinli
"""

import os
import Queue


 
exitFlag = 0
shift = input("Lutfen kayma sayisi giriniz:")
NUM_PROCESSES= input("Lutfen thread sayisini belirtiniz:")
#todo
block_lenght = input("her threadin çalışacağı block uzunluğu?")
global_file = open('metin.txt', 'r')
filename = "crypted_%d_%d_%d.txt" % (shift, NUM_PROCESSES, block_lenght)
file = open(filename, 'a')


def caesar():
    q = []
    while not exitFlag:
        if not workQueue.empty():
            plaintext = q.get()
            plaintext = plaintext.lower()
            alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",
	"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            dic={}
            for i in range(0,len(alphabet)):
                dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]
             

            ciphertext=""
            for c in plaintext:
                if c in dic:
                    c=dic[c]
                ciphertext+=c
       
            file.write(ciphertext)
        
workQueue = Queue.Queue()

children = []

for process in range(NUM_PROCESSES):
    pid = os.fork()
    if pid:
        children.append(pid) 
        print str(os.getpid())
    else:
        os._exit(0)

while True:
    string = global_file.read(NUM_PROCESSES)
    if string != '':
        workQueue.put(string)
    else:
        break

# Wait for queue to empty
while not workQueue.empty():
    pass
# Notify threads it's time to exit
exitFlag = 1
# Wait for all threads to complete

file.close()
global_file.close()
os._exit(0)
