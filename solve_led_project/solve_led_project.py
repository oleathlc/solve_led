# -*- coding: utf-8 -*-

"""Main module."""
import sys
import urllib.request
import re

def main():
    '''Checks that an argument has been given, otherwise returns and error. Then checks that the file contains something. 
    Then it converts the file to a string, takes the first line as the size of the array for our lightTester and then 
    splits the rest of the string into lines of commands and coordinates. Then it runs the lightTester method apply on 
    each line, switching the lights in the grid on/off/toggling them. Finally it runs a count on the lights left on after
    all these operations and returns the number of lights left on.'''
    if len(sys.argv)<3:
        return "Error - must have only one file as an argument e.g. solve_led_project --input text.txt"
    elif len(sys.argv)>3:
        return "Error - must have only one file as an argument e.g. solve_led_project --input text.txt"
    else:
        file = str(sys.argv[2])
        if file == None:
            return "Error - file is empty"
        else:
            instructions = readFile(file)
            firstLine = instructions.split('\n')[0]
            instructions = getCommand(instructions)
            lights=lightTester(firstLine)
            for line in instructions:
                lights.apply(line)
            return "The number occupied : ", lights.count()

if __name__ == '__solve_led_project__':
    main()

def readFile(file):
    '''Checks if the file name provided contains 'http' at the start. If so, opens and reads it as a url, otherwise, opens and reads
    it like any other file. Returns a string containing the text of the file just read'''
    commandList=""
    if file.startswith("http://"):
        url=urllib.request.urlopen(file)
        commandList=url.read().decode('utf-8') 
    else:
        commandList = open(file, 'r')
        commandList = commandList.read()
    return commandList

def getCommand(cmd):
    '''Sets a RegEx pattern and then reads a string given to it and returns all the lines that match that pattern as a set of lists
    which can be operated on'''
    pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    command = re.findall(pattern, str(cmd))
    return command

    
class lightTester():
    '''Class to create a lights grid'''
    lights=[]
    
    def __init__(self,N):
        '''Takes input N and takes as the size of the array of arrays for the grid. Every light in the grid is set to false (off).'''
        N = int(N)
        self.lights = [[False]*N for _ in range(N)]
        self.size = N
    
    def apply(self,line):
        '''Splits the RegEx lines given to it up into commands and coordinates. Checks coordinates aren't outside the range, if so 
        it amends them to fit inside. Depending on the command, turns all lights on or off or switches them based on the coordinates
        given to it'''
        start1 = int(line[1])
        start2 = int(line[2])
        end1 = int(line[3])
        end2 = int(line[4])
        if start1 < 0: #make sure start points are 0 or greater
            start1 = 0
        if start2 < 0:
            start2 = 0
        if end1 >=self.size: #make sure end points aren't greater than array size
            end1 = self.size-1
        if end2 >=self.size:
            end2 = self.size-1
        
        if (line[0] =="turn on") or (line[0] =="turn off" ) or (line[0] =="switch") :
            if line[0] == "turn on":
                if start1<=end1 and start2<=end2:
                     for i in range(start1, end1+1):
                         for j in range(start2, end2+1):
                             self.lights[i][j] = True  
            elif line[0] == "turn off":
                if start1<=end1 and start2<=end2:
                    for i in range(start1, end1+1):
                         for j in range(start2, end2+1):
                             self.lights[i][j] = False
            elif line[0] =="switch":
                if start1<=end1 and start2<=end2:
                    for i in range(start1, end1+1):
                         for j in range(start2, end2+1):
                             if self.lights[i][j] == True:
                                 self.lights[i][j]=False
                             elif self.lights[i][j] == False:
                                 self.lights[i][j]=True
        else:
            print("Invalid command!")
            
    def count(self):
        '''Checks each point in the grid to see if the light is on. For each light on it counts it and then returns the total count of lights
        that are on in the grid.'''
        count=0
        for i in range(len(self.lights)):
                for j in range(len(self.lights)):
                     if self.lights[i][j] == True: 
                         count+=1
        return count