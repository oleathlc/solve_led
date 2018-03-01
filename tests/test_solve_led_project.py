#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `solve_led_project` package."""

import pytest
from click.testing import CliRunner

from solve_led_project.solve_led_project import *

def test_checkReadUrl():
    testFile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    assert readFile(testFile)!=None

def test_checkReadFile():
    test_file = 'lineTest.txt'
    assert readFile(test_file)!= None

def test_checkCommand():
    text = "turn on 0,0 through 999,999"
    assert getCommand(text) == [('turn on', '0', '0', '999', '999')]

def test_lightTester():
    lights = lightTester(5)
    command1 = ['turn on', '0', '0', '5', '5']
    lights.apply(command1)
    print(lights.lights) #was here to check the array size
    print(lights.count()) #was here to check the count worked
    command2 = ['switch', '3', '3', '5', '5']
    lights.apply(command2)
    print(lights.lights) #was here to check the array size
    print(lights.count()) #was here to check the count worked
    command3 = ['turn off', '0', '0', '1', '1']
    lights.apply(command3)
    print(lights.lights) #was here to check the array size
    print(lights.count()) #was here to check the count worked
    assert lights.count() == 20


def test_checkArgs():
    #Not sure I can actually test this as it requires system input?
    pass
