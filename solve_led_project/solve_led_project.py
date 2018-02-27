# -*- coding: utf-8 -*-

"""Main module."""

def main(file, N):
    lights = lightTester(N)
    instructions = parse_file(file) 
    for command in instructions:
        lights.apply(cmd)
    
    print("The number occupied : ", light.count())

if __name__ == '__main__':
    main()
    
class lightTester:
    lights=None
    
    def __init__(self,N):
        self.lights = ''
    
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
    