#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
from distutils.core import setup

setup(
    options={"py2exe": {"compressed": 0, "optimize": 0, "bundle_files": 1, }},
    zipfile=None,
    console=["pysvnrpt.py"]
)
