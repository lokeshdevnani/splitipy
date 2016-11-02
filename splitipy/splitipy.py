"""
splitipy

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
  splitipy hello
  splitipu hello.mp4 --size 2000

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
        Stuff.combine(options['<file>'], options)
    elif(options['<file>']):
        Stuff.split(options['<file>'], options['--size'])

    # print("Executing bootstrap version %s." % __version__)
    # print("List of argument strings: %s" % sys.argv[1:])
    # print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))


class Boo(Stuff):
    pass
