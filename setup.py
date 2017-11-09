#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup


setup(name="x2homebank",
      version="1",
      author="Sven Festersen",
      description=" Scripts to convert transaction CSV files from online banking portals to Homebank format.",
      requires=["pandas"],
      scripts=["src/consorsbank2homebank", "src/ingdiba2homebank"],
     )
