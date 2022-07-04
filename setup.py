#!/usr/bin/env python

from setuptools import setup

setup(
    name="raw-gui",
    version="0.0.0",
    description="Raw GUI",
    author="Adarsh Melethil",
    author_email="adarshmelethil@gmail.com",
    package_dir = {'': 'lib'},
    # entry_points = {
    #     'console_scripts': ['funniest-joke=funniest.command_line:main'],
    # }
    scripts=["bin/play"],

    install_requires=[
        "hy",
        "PyOpenGL",
        "PyOpenGL_accelerate"
    ],
)
