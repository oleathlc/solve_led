#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `solve_led_project` package."""

import pytest
from click.testing import CliRunner

from solve_led_project.solve_led_project import readFile

def test_checkReadUrl():
    testFile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    assert readFile(testFile)!=None

def test_checkReadFile():
    test_file = 'lineTest.txt'
    assert readFile(test_file)!= None

def test_checkCoordinates():
    pass

def test_checkArgs():
    #Not sure I can actually test this as it requires system input?
    pass
