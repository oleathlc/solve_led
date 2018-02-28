#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `solve_led_project` package."""

import pytest
from click.testing import CliRunner

import solve_led_project
from solve_led_project import cli
from solve_led_project import readFile

def test_readCheck():
    pass

def test_checkCoordinates():
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