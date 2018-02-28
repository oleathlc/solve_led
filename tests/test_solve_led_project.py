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
    pass


'''def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'solve_led_project.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
'''