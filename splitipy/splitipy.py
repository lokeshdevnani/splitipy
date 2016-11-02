"""
splitipy

Usage:
  splitipy <file>
  splitipy -j <file> | --join <file>
  splitipy -h | --help
  splitipy --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  splitipy hello

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/lokeshthegenius/splitipy
"""

__version__ = "0.2.0"


import sys
from docopt import docopt
from .stuff import Stuff


def main():
    options = docopt(__doc__, version=__version__)
    print(options)
    if (options['-j'] or options['--join']):
        print "yay joining "+ options['<file>']
    elif(options['<file>']):
        print options['<file>']
    

    print("Executing bootstrap version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))


class Boo(Stuff):
    pass
