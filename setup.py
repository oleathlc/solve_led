#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup


setup(
    name='solve_led_project',
    version='0.1.0',
    description="Should install a console script which shows the lights that are on etc.",
    author="Conor Lawlor",
    author_email='conor.lawlor@ucdconnect.ie',
    url='https://github.com/oleathlc/solve_led_project',
    entry_points={
        'console_scripts': ['solve_led_project=solve_led_project.solve_led_project:main',],
    },
    include_package_data=True,
    license="MIT license",
    zip_safe=False,
    keywords='solve_led_project',
    test_suite='tests',
)
