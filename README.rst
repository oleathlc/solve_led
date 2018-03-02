=================
Solve Led Project
=================

Once this software has been installed from https://github.com/oleathlc/solve_led.git, it should be
installed as  a module which can be run from the command line.The module will check the size of an LED
lights grid and then read commands, turning the lights on, off or switching their status and then finally
it checks through the entire grid to see how many are left on after running all the commands. By default,
it takes a file as input and reads the file e.g.

	$ solve_led_project --input myLedGridFile.txt

It reads the first line of the file as the size of the grid of lights. Then it takes each command one at
a time, turning the lights at the provided coordinates on/off/switching them. When all commands have been
applied, it then checks the status of each light in the grid and returns the number of lights that are still
on after all the different commands.


* Free software: MIT license
* Documentation: https://solve-led-project.readthedocs.io.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
