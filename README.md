Splitipy
=====

[![PyPI](https://img.shields.io/badge/splitipy-stable-brightgreen.svg)](https://pypi.python.org/pypi/splitipy)
[![PyPI](https://img.shields.io/pypi/v/splitipy.svg)](https://pypi.python.org/pypi/splitipy)

Splitipy is a utility built with python which lets you split your files
into multiple small pieces which you can send/transfer/isolate easily
for convenience.

After you're done, gather all the pieces, run this utility again and get
back your original file.

Usage
-----

When you split a file, it will be converted into multiple parts based on
the size of the file and the max file size as passed as argument as
file.ext.1, file.ext.2, file.ext.3 and so on.

> splitipy file.ext

After you are done with the operation or transfers, to combine the file
back. Gather the pieces and run:

> splitipy --join file.ext

and it will generate the file **join-file.ext** in the same folder.

Installation
------------

Make sure you have python and pip installed and then run:

    pip install splitipy

Now, the `splitipy` command is available:

    splitipy --version 0.2.0.

On Unix-like systems, the installation places a `splitipy` script into a
centralized `bin` directory, which should be in your `PATH`. On Windows,
`splitipy.exe` is placed into a centralized `Scripts` directory which
should also be in your `PATH`.

Docs
----

### Usage:

```
splitipy <file>
splitipy <file> [--size=<mb>]
splitipy -j <file> | --join <file>
splitipy -h | --help
splitipy --version
```

### Options:

```
--help            Show this screen.
--join            Join the splitted files.
--size=<mb>       File size of each splitted file [default: 10].
--version         Show version.
```

### Examples:

Split a file named video.mp4

    splitipy video.mp4

Split file hello.mp4 with each piece size as 2000MB

    splitipy hello.mp4 --size=2000

Join the pieces together of file video.mp4 in same directory

    splitipy --join video.mp4

### Motivation
So I visited a friend and I needed to get this single large file of size 7GB from him. Problem was that we only had two pen drives of 4GB each. Now, we wanted to utilize the combined space of both the pen drives to fit in a single file, but there was no easy way to accomplish that at that moment.
So, I came up with this idea of creating a python script that could split and join binary files for easy transfers. I finished that script in less than an hour with zero to no configuration and transferred the file.

Later, I cleaned up, added a few options and documentation (thanks to docopts) and made it open source, now its available as a pip module and cli application.

### Contribute

Clone, fork, contribute and send a pull request:

<https://github.com/lokeshdevnani/splitipy>

Get in touch: <https://lokeshd.com>
