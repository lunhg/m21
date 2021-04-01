i[![Build Status](https://travis-ci.com/lunhg/m21.svg?branch=refactoring)](https://travis-ci.com/lunhg/m21)

 M21

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
$ PYTHONENV=. ./m21 --version
$ PYTHONENV=. ./m21 --help
```

## Commands

`m21` will have many subcommands. The implemented are:

  - search

### Search

Executing 

```bash
$ PYTHONENV=. ./m21 search --help
```

Show many options:

```
  -h, --help            show this help message and exit
  --actNumber ACTNUMBER
                        search for entries with actNumber predicate
  --alternativeTitle ALTERNATIVETITLE
                        search for entries with alternativeTitle predicate
  --ambitus AMBITUS     search for entries with ambitus predicate
  --associatedWork ASSOCIATEDWORK
                        search for entries with associatedWork predicate
  --collectionDesignation COLLECTIONDESIGNATION
                        search for entries with collectionDesignation
                        predicate
  --commission COMMISSION
                        search for entries with commission predicate
  --composer COMPOSER   search for entries with composer predicate
  --copyright COPYRIGHT
                        search for entries with copyright predicate
  --countryOfComposition COUNTRYOFCOMPOSITION
                        search for entries with countryOfComposition predicate
  --date DATE           search for entries with date predicate
  --dedication DEDICATION
                        search for entries with dedication predicate
  --groupTitle GROUPTITLE
                        search for entries with groupTitle predicate
  --keySignatureFirst KEYSIGNATUREFIRST
                        search for entries with keySignatureFirst predicate
  --keySignatures KEYSIGNATURES
                        search for entries with keySignatures predicate
  --localeOfComposition LOCALEOFCOMPOSITION
                        search for entries with localeOfComposition predicate
  --movementName MOVEMENTNAME
                        search for entries with movementName predicate
  --movementNumber MOVEMENTNUMBER
                        search for entries with movementNumber predicate
  --noteCount NOTECOUNT
                        search for entries with noteCount predicate
  --number NUMBER       search for entries with number predicate
  --numberOfParts NUMBEROFPARTS
                        search for entries with numberOfParts predicate
  --opusNumber OPUSNUMBER
                        search for entries with opusNumber predicate
  --parentTitle PARENTTITLE
                        search for entries with parentTitle predicate
  --pitchHighest PITCHHIGHEST
                        search for entries with pitchHighest predicate
  --pitchLowest PITCHLOWEST
                        search for entries with pitchLowest predicate
  --popularTitle POPULARTITLE
                        search for entries with popularTitle predicate
  --quarterLength QUARTERLENGTH
                        search for entries with quarterLength predicate
  --sceneNumber SCENENUMBER
                        search for entries with sceneNumber predicate
  --sourcePath SOURCEPATH
                        search for entries with sourcePath predicate
  --tempoFirst TEMPOFIRST
                        search for entries with tempoFirst predicate
  --tempos TEMPOS       search for entries with tempos predicate
  --textLanguage TEXTLANGUAGE
                        search for entries with textLanguage predicate
  --textOriginalLanguage TEXTORIGINALLANGUAGE
                        search for entries with textOriginalLanguage predicate
  --timeSignatureFirst TIMESIGNATUREFIRST
                        search for entries with timeSignatureFirst predicate
  --timeSignatures TIMESIGNATURES
                        search for entries with timeSignatures predicate
  --title TITLE         search for entries with title predicate
  --volume VOLUME       search for entries with volume predicate
```

#### Search Example:

A simple search will return a string representation of Namespace class:

```bash
$ PYTHONPATH=. ./m21 search --composer mozart

Namespace(subcommand='search', ..., composer={'name': 'mozart', 'results': [...]}, ...)
```

# Test

```bash
$ tox
```

# TODO

    - in search, return a json representation of an object
