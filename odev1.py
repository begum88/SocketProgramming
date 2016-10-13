#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:43:57 2016

@author: begumpasinli
"""
from pyemd import emd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


fig = plt.figure()


mu1 = 4 # dağılımın ortalaması
sigma1 = 0.6 # standart sapması
mu2 = 0
sigma2 =1
x1 = mu1 + sigma1 * np.random.randn(10000)
x2 = mu2 + sigma2 * np.random.randn(10000)

# -20'den +20'ye kadar olan değerler arasında bir histogram çizdiriyoruz
num_bins = [-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# verinin histogramı
n, bins, patches = plt.hist(x2, num_bins, normed=1, facecolor='blue', alpha=0.5) 
# en uygun çizgileri eklemek için fonksiyon
y2 = mlab.normpdf(bins, mu2, sigma2)
plt.plot(bins, y2, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')

plt.subplots_adjust(left=0.20)



n, bins, patches = plt.hist(x1, num_bins, normed=1, facecolor='green', alpha=0.5) 
y1 = mlab.normpdf(bins, mu1, sigma1)
plt.plot(bins, y1, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')


plt.subplots_adjust(left=0.20)
# Aşağıdaki kod iki histogramın birbirine olan uzaklığını ölçüyor ama
#kullanmamız için first ve second signature'ü belirlememiz lazım 
#ben de ağırlıklı x eksenleri neredeyse ona göre belirlemek istedim
first_signature = np.array([-5.0, 5.0]) #mavi grafiğin ağırlıklı dağımı bu arada
second_signature = np.array([0.0, 5.0]) # yeşil grafik ise bu arada
distance_matrix = np.array([ y1,y2 ])
distance = (emd(first_signature, second_signature, distance_matrix))
print ("distance =",  distance)



