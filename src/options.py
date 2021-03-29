# BaseURL to reuse
__baseUrl__ = "http://web.mit.edu/music21/doc/systemReference"

GRAPHICAL_ANALYSIS_options = [
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

options = []
##########################################
# STRUCTURE OF VARIABLES
# OPTION_CONST = [
#  short_option,
#  long_option
#  option_type (feed a value or a boolean)
#  help_text
# ]
##########################################
gui = []
gui.append("G")
gui.append("gui")
gui.append("store_true")
gui.append("start m21 with Graphical User Interface")
options.append(gui)

search = []
search.append("s")
search.append("search")
search.append("store_true")
search.append("\n\t".join([
    "Search in corpus for words in --composer and or --index arguments.",
    "Ex.: --composer bach --index bwv1x"
]))

options.append(search)

composer = []
composer.append("c")
composer.append("composer")
composer.append(None)
composer.append("\n\t".join([
    "write report with specific corpora.",
    "CAUTION: you must use this according",
    __baseUrl__ + "/referenceCorpus.html#referencecorpus"
]))
options.append(composer)

index = []
index.append("i")
index.append("index")
index.append(None)
index.append("\n\t".join([
    "Search in corpus a specific index of corpora;",
    "you must use this with -c option",
    "according available corpora in",
    __baseUrl__ + "/referenceCorpus.html#referencecorpus"
]))
options.append(index)

cac = []
cac.append("C")
cac.append("cac")
cac.append("store_true")
cac.append("\n\t".join([
    "Or simple \"Computer Assisted Composition\".",
    "With this option you will \"glitch\" a specific piece,",
    "as instance, with --composer/--index options, --xml option",
    "or --tiny-notation option.",
    "Adding --fragmentize option with a value",
    "(ex: --fragmentize <N>, from 0 up to 6)",
    "you will apply a \"fragmentation\" on input.",
    "You can add --no-scramble-notes, --no-scramble-octaves and  arguments."
]))
options.append(cac)

no_scramble_notes = []
no_scramble_notes.append("n")
no_scramble_notes.append("no-scramble-notes")
no_scramble_notes.append("store_true")
no_scramble_notes.append("\n\t".join([
    "with this option, the program will not apply",
    "a scramble on list of extracted notes, before create chords"
]))
options.append(no_scramble_notes)

no_scramble_octaves = []
no_scramble_octaves.append("N")
no_scramble_octaves.append("no-scramble-octaves")
no_scramble_octaves.append("store_true")
no_scramble_octaves.append("\n\t".join([
    "With this option, the program will not apply a scramble in a list",
    "of extracted octaves, before create chords"
]))
options.append(no_scramble_octaves)

glitch = []
glitch.append("g")
glitch.append("glitch")
glitch.append(None)
glitch.append("\n\t".join([
    "Apply a\'glitch\' on extracted notes and octaves;",
    "the given argument is the maximum of a random operation.",
    "This operation can be a choice of a 6 values:",
    "(0) The generated chord will be arranged in closed position;",
    "(1) the generated chord will be arranged in semi-closed position;",
    "(2) the generated chord will be arranged in super open position;",
    "(3) one note will be separated from chord, like an one grace note;",
    "(4) two notes will be separated from chord" +
    "(if this chord have at least, two notes);",
    "(5) apply bordadure [? translate ?], and then a chord"
]))
options.append(glitch)

measures = []
measures.append("m")
measures.append("measures")
measures.append(None)
measures.append("\n\t".join([
    "Select measures from a stream (corpus, xml or tinynotation)"
]))
options.append(measures)

REDUCTE = []
REDUCTE.append("R")
REDUCTE.append("reducte")
REDUCTE.append("store_true")
REDUCTE.append("Reducte some stream to piano staff ")
options.append(REDUCTE)

TONAL_HARMONIC_ANALYSIS = []
TONAL_HARMONIC_ANALYSIS.append("A")
TONAL_HARMONIC_ANALYSIS.append("tonal-harmonic-analysis")
TONAL_HARMONIC_ANALYSIS.append(None)
TONAL_HARMONIC_ANALYSIS.append("\n\t".join([
    "Analyse some stream in tonal way,"
    "given some key"
]))
options.append(TONAL_HARMONIC_ANALYSIS)

SHOW = []
SHOW.append("S")
SHOW.append("show")
SHOW.append("store_true")
SHOW.append("show stream in some editor (default: musescore)")
options.append(SHOW)

XML = []
XML.append("x")
XML.append("xml")
XML.append(None)
XML.append("parse a musicXml file; can be a local one or http url")
options.append(XML)

TINY_NOTATION = []
TINY_NOTATION.append("t")
TINY_NOTATION.append("tinynotation")
TINY_NOTATION.append(None)
TINY_NOTATION.append("\n\t".join([
    "parse a tiny-notation",
    "ex: --tiny-notation \"2/16 E4 r f# g=lastG trip{b-8 a g} c\"."
]))
options.append(TINY_NOTATION)

TITLE = []
TITLE.append("T")
TITLE.append("title")
TITLE.append(None)
TITLE.append("\n\t".join([
    "used to give a title.",
    "(ex: --title \"My improvised music\""
]))
options.append(TITLE)

AUTHOR = []
AUTHOR.append("a")
AUTHOR.append("author")
AUTHOR.append(None)
AUTHOR.append("used to give a author's piece. (ex: --author \"J.S. Bach\"")
options.append(AUTHOR)

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
options.append(TRANSPOSE)

INVERT = []
INVERT.append("I")
INVERT.append("invert")
INVERT.append("store_true")
INVERT.append("invert stream intervals by semitones. No need arguments")
options.append(INVERT)

LYTEXIFY = []
LYTEXIFY.append("L")
LYTEXIFY.append("lytexify")
LYTEXIFY.append(None)
LYTEXIFY.append("\n\t".join([
    "Create a .lytex file from a .ly file,"
    "and compiles it to a .tex file.",
    "Used only in the context of documentation of this software"
]))
options.append(LYTEXIFY)
