#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:11:08 2016

@author: begumpasinli
"""
import Queue
import threading

exitFlag = 0
shift = input("Lutfen kayma sayisi giriniz:")
num_thread = input("Lutfen thread sayisini belirtiniz:")
#todo
block_lenght = input("her threadin çalışacağı block uzunluğu?")
global_file = open('metin.txt', 'r')
filename = "crypted_%d_%d_%d.txt" % (shift, num_thread, block_lenght)
file = open(filename, 'a')
#thread oluşturma örneğine bakmak için : https://www.tutorialspoint.com/python/python_multithreading.htm

class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print "Starting " + self.name
        caesar(self.name, self.q)
        print "Exiting " + self.name
        

def caesar(threadName, q):
    while not exitFlag:
        queueLock.acquire()
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
            queueLock.release()
        else:
            queueLock.release()

queueLock = threading.Lock()
workQueue = Queue.Queue()

threadID = 0

# Create new threads
threads = []
for n in range(num_thread):
    thread = myThread(threadID, 'thread_' + str(threadID), workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
# Fill the queue
while True:
    string = global_file.read(num_thread)
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
for t in threads:
    t.join()

file.close()
global_file.close()

print "Exiting Main Thread"
