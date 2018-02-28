# -*- coding: utf-8 -*-

"""Main module."""
import sys
import urllib.request

def main():
    lights = lightTester(N)
    file = checkArgs()
    if file == None:
        return "Error"
    else:
        instructions = readFile(file) 
        for command in instructions:
            lights.apply(cmd)
    
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
    # Rough idea of how file should be read. Will likely
    # need to put it elsewhere
    commandList=""
    if file.startswith("http://"):
        url=urllib.request.urlopen(file)
        commandList=url.read().decode('utf-8')
    else:
        commandList = open(file, 'r')
        commandList.read() 
    return commandList

def getCoordinates(list):
    #read first line of the commandList to read the number of lines
    pass
    
    
class lightTester():
    lights=[]
    
    def __init__(self,N):
        self.lights = [[False]*size for _ in range(size)]
    
    def apply(self,cmd):
        if cmd == "turn on":
            pass
        elif cmd == "turn off":
            pass
        elif cmd == "switch":
            pass
        else:
            print("Invalid command!")
            
    def count(self):
        pass
        return count
