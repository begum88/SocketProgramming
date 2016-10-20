#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:00:18 2016

@author: begumpasinli
"""

import numpy as np
f=open("Metin.txt","r")
plaintext=f.read
print plaintext
    
    
class airlineProblem:
     @staticmethod
     def main():
         try:
           f =open("airlines.txt.rtf","r") 
           airline = f.read()
           airline = airline[292:]
           #print airline
           #print type (airline)
         except IOError: 
           print "Could not connect to file airlines.txt."
        
         if airline != " ":
            airline = airline.split()
            airline = [c.replace(' ','')for c in airline]
            airline ="".join(airline)
            #print airline
            airline = airline.split()
            airline = [c.replace('\\','\n')for c in airline]
            airlinesName ="".join(airline)
            airlinesName = [c.replace(',','\n')for c in airline]
            airlinesName ="".join(airline)
            print airlinesName

if  __name__ == "__main__":
     airlineProblem.main()
     
     
     
     
     
     
     
class bool:
    @staticmethod
    def __init__(self):
        self.current=""
        self.goals=""
        self.pathForMiles= []
        self.airlinesVisited = []
        self.network=[]
    def _canRedeem(self,current,goals,pathForMiles,airlinesVisited,network):
          if self.current is self.goals:
              self.pathForMiles.append(self.current)
              return True
          elif (self.current in self.airlinesVisited):  
              return False
          else:
              self.airlinesVisited.append(current)
              self.pathForMiles.append(current)
              pos = -1
              index =0
              while pos == -1 and index < len(self.network):
                  if self.current in self.network.index:
                      pos = index
                  index = index +1
          if pos == -1:
              return False
          index = 0
          partners = Airline.getPartners(self.network)
          foundPath = False
          while foundPath==False and index <len(partners):
             foundPath= bool._canRedeem(partners[index],self.goals,self.pathForMiles,self.airlinesVisited,self.network)
             index = index + 1
          if foundPath == False:
              self.pathForMiles.remove(len(self.pathForMiles)-1)
          return foundPath
          
          
          
                  
              
             
      
          
        
       
  
                  
                  
                  
class Airline:
    @staticmethod
    def __init__(self):
        self.name = ""
        self.partners = []
    def _partners(self):
        self.partners.contains=None
    def Airline(self,data):
        assert data!= "" , len(data) >0
        self.name = data[0]
        for i in range(1,len(data)):
            self.partners.append(data(i))
    def getPartners(self ,partners):
        self.partners= np.asarray(partners)
        return partners
    def isPartner(self)    :
        val = self.partners.contains(self.name)
        return val
    def getName(self):
        return self.name
    def toString(self):
        return self.name + ("partners") + self.partners

        
        
        
        
          
            



        
        

     
     
     
    
        