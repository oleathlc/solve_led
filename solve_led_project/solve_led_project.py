# -*- coding: utf-8 -*-

"""Main module."""
import sys
import urllib.request
import re

def main():
    lights = lightTester(N)
    file = checkArgs()
    if file == None:
        return "Error"
    else:
        instructions = readFile(file)
        for line in instructions:
            lights.apply(line)
    
            return "The number occupied : " + light.count()

if __name__ == '__main__':
    main()

    
def checkArgs():
    if len(sys.argv)<3:
        return
    elif len(sys.argv)>3:
        return
    else:
        args=str(sys.argv)
        return args[2]
        
def readFile(file):
    commandList=""
    if file.startswith("http://"):
        url=urllib.request.urlopen(file)
        commandList=url.read().decode('utf-8')
    else:
        commandList = open(file, 'r')
        commandList.read() 
    return commandList

    
class lightTester():
    lights=[]
    
    def __init__(self,N):
        self.lights = [[False]*N for _ in range(size)]
        self.size = N
        
    def getCoordinates(self,cmd):
        pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        command = re.findall(pattern, str(cmd))
        return command
    
    def apply(self,line):
        line = getCoordinates(line)
        start1 = int(line[1])
        start2 = int(line[2])
        end1 = int(line[3])
        end2 = int(line[4])
        
        if start1 < 0: #make sure start points are 0 or greater
            start1 = 0
        if start2 < 0:
            start2 = 0
        if end1 >self.size-1: #make sure end points aren't greater than size
            end1 = self.size-1
        if end2 >self.size-1:
            end2 = self.size-1
        
        if (line[0] =="turn on") or (line[0] =="turn off" ) or (line[0] =="switch") :
            if line[0] == "turn on":
                 for i in range(start1, end1):
                     for j in range(start2, end2):
                         self.light[i][j] = True
                 
            elif line[0] == "turn off":
                for i in range(start1, end1):
                     for j in range(start2, end2):
                         self.light[i][j] = False
            elif line[0] =="switch":
                for i in range(start1, end1):
                     for j in range(start2, end2):
                         if self.light[i] == True:
                             self.light[i]=False
                         else:
                             self.light[i]==True
                         if self.light[j] == True:
                             self.light[j]=False
                         else:
                             self.light[j]==True
        else:
            print("Invalid command!")
            
    def count(self):
        pass
        return count
    
    
    
    
