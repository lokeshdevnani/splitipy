========
Splitipy
========

Splitipy is a utility built with python which lets you split your files into multiple small pieces which you can send/transfer/isolate easily for convenience.

After you're done, gather all the pieces, run this utility again and get back your original file.


Usage
-----

When you split a file, it will be converted into multiple parts based on the size of the file and the max file size as passed as argument as
file.ext.1, file.ext.2, file.ext.3 and so on.

  splitipy file.ext

After you are done with the operation or transfers, to combine the file back. Gather the pieces and run:

  splitipy --join file.ext

and it will generate the file **join-file.ext** in the same folder.


Installation
------------

Make sure you have python and pip installed and then run:

    >>> pip install splitipy

Situation before installation:

    >>> splitipy
    bash: splitipy: command not found

Now, the ``splitipy`` command is available:

    >>> splitipy --version
    0.2.0.

On Unix-like systems, the installation places a ``splitipy`` script into a
centralized ``bin`` directory, which should be in your ``PATH``. On Windows,
``splitipy.exe`` is placed into a centralized ``Scripts`` directory which
should also be in your ``PATH``.


Docs
-----

Usage:
^^^^^^

 -  splitipy <file>
 -  splitipy <file> [--size=<mb>]
 -  splitipy -j <file> | --join <file>
 -  splitipy -h | --help
 -  splitipy --version

Options:
^^^^^^^^

  --help                            Show this screen.
  --join                            Join the splitted files.
  --size=<mb>                       File size of each splitted file [default: 10].
  --version                         Show version.

Examples:
^^^^^^^^^

    splitipy video.mp4

    splitipy hello.mp4 --size=2000

    splitipy --join video.mp4


Contribute
----------

Clone, fork, contribute and send a pull request:

https://github.com/lokeshthegenius/splitipy

Get in touch: https://lokeshd.com
