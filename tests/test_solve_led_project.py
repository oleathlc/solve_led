#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `solve_led_project` package."""
import sys
sys.path.append('.')
import pytest
from solve_led_project.solve_led_project import *

def test_checkReadUrl():
    '''Checks that the readFile function works to read input from an online text file returning a string'''
    testFile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    assert readFile(testFile)!=None

def test_checkReadFile():
    '''Checks that the readFile function works to read input from a local text file returning a string'''
    test_file = 'lineTest.txt'
    assert readFile(test_file)!= None

def test_checkCommand():
    '''Checks that the getCommand method works to split the file string up into lines containing a list which
    we can index and divide into commands and coordinates'''
    test = [('turn on 0,0 through 999,999)')]
    assert getCommand(test) == [('turn on', '0', '0', '999', '999')]

def test_lightTester():
    '''Checks the lightTester class. Creates a new class, and then runs the apply method on different commands
    and coordinates, and then confirms the count function also works correctly by comparing it to a figure which
    will match the lights which should be on after the operations that were carried out'''
    lights = lightTester(5)
    command1 = ['turn on', '0', '0', '5', '5']
    lights.apply(command1)
    #print(lights.lights) #was here to check the array size
    #print(lights.count()) #was here to check the count worked
    command2 = ['switch', '3', '3', '5', '5']
    lights.apply(command2)
    #print(lights.lights) 
    #print(lights.count()) 
    command3 = ['turn off', '0', '0', '1', '1']
    lights.apply(command3)
    #print(lights.lights)
    #print(lights.count())
    assert lights.count() == 20