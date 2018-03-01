# -*- coding: utf-8 -*-

"""Main module."""
import sys
import urllib.request
import re

def main():
    #file = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'
    if len(sys.argv)<3: #file == 0: #
        return
    elif  len(sys.argv)>3: #file == 1: #
        return
    else:
        file = str(sys.argv[2])
        if file == None:
            return "Error"
        else:
            instructions = readFile(file)
            firstLine = instructions.split('\n')[0]
            instructions = getCommand(instructions)
            rest = instructions[1:]
            lights=lightTester(firstLine)
            for line in rest:
                lights.apply(line)
            return "The number occupied : ", lights.count()

if __name__ == '__main__':
    main()

def readFile(file):
    commandList=""
    if file.startswith("http://"):
        url=urllib.request.urlopen(file)
        commandList=url.read().decode('utf-8') 
    else:
        commandList = open(file, 'r')
    return commandList

def getCommand(cmd):
        pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        command = re.findall(pattern, str(cmd))
        return command

    
class lightTester():
    lights=[]
    
    def __init__(self,N):
        N = int(N)
        self.lights = [[False]*N for _ in range(N)]
        self.size = N
    
    def apply(self,line):
        start1 = int(line[1])
        start2 = int(line[2])
        end1 = int(line[3])
        end2 = int(line[4])
        if start1 < 0: #make sure start points are 0 or greater
            start1 = 0
        if start2 < 0:
            start2 = 0
        if end1 >self.size: #make sure end points aren't greater than array size
            end1 = self.size-1
        if end2 >self.size-1:
            end2 = self.size
        
        if (line[0] =="turn on") or (line[0] =="turn off" ) or (line[0] =="switch") :
            if line[0] == "turn on":
                if start1<=end1 and start2<=end2:
                     for i in range(start1, end1):
                         for j in range(start2, end2):
                             self.lights[i][j] = True  
            elif line[0] == "turn off":
                if start1<=end1 and start2<=end2:
                    for i in range(start1, end1):
                         for j in range(start2, end2):
                             self.lights[i][j] = False
            elif line[0] =="switch":
                if start1<=end1 and start2<=end2:
                    for i in range(start1, end1):
                         for j in range(start2, end2):
                             if self.lights[i][j] == True:
                                 self.lights[i][j]=False
                             elif self.lights[i][j] == False:
                                 self.lights[i][j]=True
        else:
            print("Invalid command!")
            
    def count(self):
        count=0
        for i in range(len(self.lights)):
                for j in range(len(self.lights)):
                     if self.lights[i][j] == True: 
                         count+=1
        return count
    
print(main())