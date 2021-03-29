[![Build Status](https://travis-ci.com/lunhg/m21.svg?branch=refactoring)](https://travis-ci.com/lunhg/m21)

# M21

M21 is an CLI and GUI (in process) that use [Music21](https://github.com/cuthbertLab/music21).

The main purpose of the software is to assist composers and analysts to automate some common compositional and analysis routines (at least from the point of view of the author of this repository)

# Documentation

All documentation is available in the doc folder, with examples in the examples folder 

# Installing:

```bash
$ git clone https://github.com/lunhg/m21.git
```

# Executing
```bash
$ PYTHONENV=. python src/cli.py --version
$ PYTHONENV=. python src/cli.py --help
$ PYTHONENV=. python src/cli.py search --composer bach
$ PYTHONENV=. python src/cli.py search --index bwv1
$ PYTHONENV=. python src/cli.py search --composer bach --index bwv123 
```

# Test

```bash
$ tox
```
