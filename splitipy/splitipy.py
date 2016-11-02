"""
splitipy
========
Split your file into multiple small pieces and easily transfer them using removable media.

Usage:
  splitipy <file>
  splitipy <file> [--size=<mb>]
  splitipy -j <file> | --join <file>
  splitipy -h | --help
  splitipy --version

Options:
  -h --help                         Show this screen.
  --size=<mb>                       File size of each splitted file [default: 10].
  --version                         Show version.

Examples:
  splitipy video.mp4
  splitipy hello.mp4 --size=2000
  splitify --join video.mp4

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/lokeshthegenius/splitipy
"""

__version__ = "1.0.0"


import sys
from docopt import docopt
from .stuff import Stuff

def main():
    options = docopt(__doc__, version=__version__)
    if (options['-j'] or options['--join']):
        Stuff.combine(options['<file>'])
    elif(options['<file>']):
        Stuff.split(options['<file>'], options['--size'])

class Boo(Stuff):
    pass
