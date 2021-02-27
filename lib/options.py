# BaseURL to reuse
__baseUrl__ = "http://web.mit.edu/music21/doc/systemReference"

GRAPHICAL_ANALYSIS_OPTIONS = [
    "PlotStream",
    "PlotHistogramPitchSpace",
    "PlotHistogramPitchClass",
    "PlotHistogramQuarterLength",
    "PlotScatterPitchSpaceQuarterLength",
    "PlotScatterPitchClassQuarterLength",
    "PlotScatterPitchClassOffset",
    "PlotScatterPitchSpaceDynamicSymbol",
    "PlotHorizontalBarPitchSpaceOffset",
    "PlotHorizontalBarPitchClassOffset",
    "PlotScatterWeightedPitchSpaceQuarterLength",
    "PlotScatterWeightedPitchClassQuarterLength",
    "PlotScatterWeightedPitchSpaceDynamicSymbol",
    "Plot3DBarsPitchSpaceQuarterLength",
    "PlotWindowedKrumhanslSchmuckler",
    "PlotWindowedKrumhanslKesslerm",
    "PlotWindowedAardenEssen",
    "PlotWindowedSimpleWeights",
    "PlotWindowedBellmanBudge",
    "PlotWindowedTemperleyKostkaPayne",
    "PlotWindowedAmbitus",
    "PlotDolan"
]

OPTIONS = []
##########################################
# STRUCTURE OF VARIABLES
# OPTION_CONST = [
#  short_option,
#  long_option
#  option_type (feed a value or a boolean)
#  help_text
# ]
##########################################
GUI = []
GUI.append("G")
GUI.append("gui")
GUI.append("store_true")
GUI.append("start m21 with Graphical User Interface")
OPTIONS.append(GUI)

SEARCH_ONLY = []
SEARCH_ONLY.append("s")
SEARCH_ONLY.append("search-only")
SEARCH_ONLY.append("store_true")
SEARCH_ONLY.append("\n\t".join([
    "Search in corpus for words in --composer and or --index arguments.",
    "Ex.: --composer bach --index bwv1x"
]))
OPTIONS.append(SEARCH_ONLY)

COMPOSER = []
COMPOSER.append("c")
COMPOSER.append("composer")
COMPOSER.append(None)
COMPOSER.append("\n\t".join([
    "write report with specific corpora.",
    "CAUTION: you must use this according",
    __baseUrl__ + "/referenceCorpus.html#referencecorpus"
]))
OPTIONS.append(COMPOSER)

INDEX = []
INDEX.append("i")
INDEX.append("index")
INDEX.append(None)
INDEX.append("\n\t".join([
    "Search in corpus a specific index of corpora;",
    "you must use this with -c option",
    "according available corpora in",
    __baseUrl__ + "/referenceCorpus.html#referencecorpus"
]))
OPTIONS.append(INDEX)

CAC = []
CAC.append("C")
CAC.append("cac")
CAC.append("store_true")
CAC.append("\n\t".join([
    "Or simple \"Computer Assisted Composition\".",
    "With this option you will \"glitch\" a specific piece,",
    "as instance, with --composer/--index options, --xml option",
    "or --tiny-notation option.",
    "Adding --fragmentize option with a value",
    "(ex: --fragmentize <N>, from 0 up to 6)",
    "you will apply a \"fragmentation\" on input.",
    "You can add --no-scramble-notes, --no-scramble-octaves and  arguments."
]))
OPTIONS.append(CAC)

NO_SCRAMBLE_NOTES = []
NO_SCRAMBLE_NOTES.append("n")
NO_SCRAMBLE_NOTES.append("no-scramble-notes")
NO_SCRAMBLE_NOTES.append("store_true")
NO_SCRAMBLE_NOTES.append("\n\t".join([
    "with this option, the program will not apply",
    "a scramble on list of extracted notes, before create chords"
]))
OPTIONS.append(NO_SCRAMBLE_NOTES)

NO_SCRAMBLE_OCTAVES = []
NO_SCRAMBLE_OCTAVES.append("N")
NO_SCRAMBLE_OCTAVES.append("no-scramble-octaves")
NO_SCRAMBLE_OCTAVES.append("store_true")
NO_SCRAMBLE_OCTAVES.append("\n\t".join([
    "With this option, the program will not apply a scramble in a list",
    "of extracted octaves, before create chords"
]))
OPTIONS.append(NO_SCRAMBLE_OCTAVES)

GLITCH = []
GLITCH.append("g")
GLITCH.append("glitch")
GLITCH.append(None)
GLITCH.append("\n\t".join([
    "Apply a\'glitch\' on extracted notes and octaves;",
    "the given argument is the maximum of a random operation.",
    "This operation can be a choice of a 6 values:",
    "(0) The generated chord will be arranged in closed position;",
    "(1) the generated chord will be arranged in semi-closed position;",
    "(2) the generated chord will be arranged in super open position;",
    "(3) one note will be separated from chord, like an one grace note;",
    "(4) two notes will be separated from chord (if this chord have at least, two notes);",
    "(5) apply bordadure [? translate ?], and then a chord"
]))
OPTIONS.append(GLITCH)

MEASURES = []
MEASURES.append("m")
MEASURES.append("measures")
MEASURES.append(None)
MEASURES.append("\n\t".join([
    "Select measures from a stream (corpus, xml or tinynotation"
]))
OPTIONS.append(MEASURES)

REDUCTE = []
REDUCTE.append("R")
REDUCTE.append("reducte")
REDUCTE.append("store_true")
REDUCTE.append("Reducte some stream to piano staff ")
OPTIONS.append(REDUCTE)

TONAL_HARMONIC_ANALYSIS = []
TONAL_HARMONIC_ANALYSIS.append("A")
TONAL_HARMONIC_ANALYSIS.append("tonal-harmonic-analysis")
TONAL_HARMONIC_ANALYSIS.append(None)
TONAL_HARMONIC_ANALYSIS.append("\n\t".join([
    "Analyse some stream in tonal way,"
    "given some key"
]))
OPTIONS.append(TONAL_HARMONIC_ANALYSIS)

SHOW = []
SHOW.append("S")
SHOW.append("show")
SHOW.append("store_true")
SHOW.append("show stream in some editor (default: musescore)")
OPTIONS.append(SHOW)

XML = []
XML.append("x")
XML.append("xml")
XML.append(None)
XML.append("parse a musicXml file; can be a local one or http url")
OPTIONS.append(XML)

TINY_NOTATION = []
TINY_NOTATION.append("t")
TINY_NOTATION.append("tinynotation")
TINY_NOTATION.append(None)
TINY_NOTATION.append("\n\t".join([
    "parse a tiny-notation",
    "ex: --tiny-notation \"2/16 E4 r f# g=lastG trip{b-8 a g} c\"."
]))
OPTIONS.append(TINY_NOTATION)

TITLE = []
TITLE.append("T")
TITLE.append("title")
TITLE.append(None)
TITLE.append("\n\t".join([
    "used to give a title.",
    "(ex: --title \"My improvised music\""
]))
OPTIONS.append(TITLE)

AUTHOR = []
AUTHOR.append("a")
AUTHOR.append("author")
AUTHOR.append(None)
AUTHOR.append("used to give a author's piece. (ex: --author \"J.S. Bach\"")
OPTIONS.append(AUTHOR)

TRANSPOSE = []
TRANSPOSE.append("r")
TRANSPOSE.append("transpose")
TRANSPOSE.append(None)
TRANSPOSE.append("\n\t".join([
    "transpose stream notes by semitones",
    "(ex.: --transpose 4 will transpose to",
    "a ascendent major third",
    "and --transpose -4 will transpose to a descendent major third"
]))
OPTIONS.append(TRANSPOSE)

INVERT = []
INVERT.append("I")
INVERT.append("invert")
INVERT.append("store_true")
INVERT.append("invert stream intervals by semitones. No need arguments")
OPTIONS.append(INVERT)

LYTEXIFY = []
LYTEXIFY.append("L")
LYTEXIFY.append("lytexify")
LYTEXIFY.append(None)
LYTEXIFY.append("\n\t".join([
    "Create a .lytex file from a .ly file,"
    "and compiles it to a .tex file.",
    "Used only in the context of documentation of this software"
]))
OPTIONS.append(LYTEXIFY)
