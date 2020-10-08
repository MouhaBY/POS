"""Fichier d'installation de notre script main.py."""

import sys

from cx_Freeze import setup, Executable


#main
exe = Executable(script="main.py", base="Win32GUI")

buildOptions = dict(excludes = [], includes =[], packages = ["images",], optimize=1)

setup(
    name = "POS",
    version = "1.01",
    description = "test",
    executables = [exe],
    options =dict(build_exe = buildOptions)
)