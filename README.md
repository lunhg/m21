# M21

M21 is an CLI and GUI (in process) that use [Music21](https://github.com/cuthbertLab/music21).

The main purpose of the software is to assist composers and analysts to automate some common compositional and analysis routines (at least from the point of view of the author of this repository)

# Documentation

All documentation is available in the doc folder, with examples in the examples folder 

# Installing:

```bash
$ git clone https://github.com/lunhg/m21.git
$ cd m21 && chmod +x ./m21
```

# Test

```bash
$ tox
```

# Usage

## Help

Show the CLI help

``bash
$ ./m21 --help`
``

## Example of compositional material with pre-existing music in corpora

This apply  a Computer Assisted Composition (`--CAC`) with a glitch techinique (`--glitch`) for a pre-existing Bach's music in [Music21 Corpus](https://web.mit.edu/music21/doc/moduleReference/moduleCorpusCorpora.html#corpus) (`--composer` and `--index bwv1`) and shows the generated material in Musescore:

``bash
$ ./m21.py --show --CAC --composer bach --index bwv1 --glitch 2
``

## Example of analysis material

This apply a Computer Assisted Analysis with a Ploting of a pitch space's histogram (`--plot-histogram-pitch-space`) in a pre-existing Bach's music in [Music21 Corpus](https://web.mit.edu/music21/doc/moduleReference/moduleCorpusCorpora.html#corpus) (`--composer` and `--index bwv1`) and show it in Musescore:

``bash
$ ./m21 --show --composer bach --index bwv1 --plot-histogram-pitch-space
``

## Aimed usage with graphical interface

```bash
$ m21 --gui
```

# TODO

- An Tkinter Graphical User Interface
- Menu interfaces:
  - New, Open, Save, etc.
  - Edit, Copy, Cut, Paste, etc.
  - Tools: all tools presented in CLI
- Text editor to customize analysis or compositional routines
