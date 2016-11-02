# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('splitipy/splitipy.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "splitipy",
    packages = ["splitipy"],
    entry_points = {
        "console_scripts": ['splitipy = splitipy.splitipy:main']
        },
    version = version,
    description = "Python CLI application to split and join files for easy transfer via external media.",
    long_description = long_descr,
    author = "Lokesh Devnani",
    author_email = "contact@lokeshd.com",
    url = "https://github.com/lokeshthegenius/splitipy",
    )
