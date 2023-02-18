#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(name="x2homebank",
      version="2.0.0",
      author="Sven Rusch",
      author_email="sven@sven-rusch.de",
      description=" Scripts to convert transaction CSV files from online banking portals to Homebank format.",
      packages=find_packages(where="src"),
      package_dir={"": "src"},
      entry_points={"console_scripts": [
            "x2homebank = x2homebank.cli.homebank:main",
            "consorsbank2homebank = x2homebank.cli.consorsbank:main",
            "ing2homebank = x2homebank.cli.ing:main",
      ]},
      install_requires=["click"]
      )
