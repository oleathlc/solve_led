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
    command = ['turn on', '0', '0', '5', '5']
    lights.apply(command)
    #print(lights.lights) #was here to check the array size
    #print(lights.count()) #was here to check the count worked
    assert lights.count() == 25


def test_checkArgs():
    #Not sure I can actually test this as it requires system input?
    pass
