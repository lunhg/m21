from music21 import *
import math
import random
import datetime
#import re

# Funcoes
def rnd(max):
    """Um numero randomico"""
    return math.floor(random.random() * max)
    

def search_stream(options):
    """Procura por um stream no corpus"""
    if not options.index and options.composer:
        s = options.composer
    elif not options.composer and options.index:
        s = options.index
    elif options.composer and options.index:
        s = "%s/%s" % (options.composer, options.index)
    metadata = corpus.search(s)
    print("m21> found %d entries for %s" % (len(metadata), s))
    return metadata

def choice_measures(part):
    """Escolhe randomicamente uma secao da peca para ser modificada"""
    l = len(part.measureOffsetMap())
    r = [int(rnd(l)) for i in [0, 1]]
    a = min(r[0], r[1])
    b = max(r[0], r[1])

    if(not b>a):
        b = a + 1

    print("measures: %d:%d" % (a, b))
    matrix = [measure for measure in part.measures(a, b)]
    return [matrix[i] for i in range(4,len(matrix))]

def verify_and_map_notes_in_measure(element):
    """Checar se existe alguma estrutura xml que engloba as notas; verificado aps extracao de algumas pecas do mozart"""
    _dict = {"notes": [], "octaves": []} 
    looper =  None
    print(element.classes)
    if element.classes[0] == 'Slur':
        looper = element.getSpannedElements()
    elif element.classes[0] == 'Measure':
        looper = element.notes
    
    for el in looper:
        if el.classes[0] == 'Chord':
            for p in el.pitches:
                _dict["notes"].append(str(p.name))
                _dict["octaves"].append(str(p.octave))
        else:
            _dict["notes"].append(str(el.pitch.name))
            _dict["octaves"].append(str(el.octave))

    return _dict

def scramble_notes_if(_dict, options):
    """Scramble dictionary of notes and octaves"""
    print(_dict)
    if not options.no_scramble_notes: 
        _dict["notes"] = sorted(_dict["notes"], key = lambda x: random.random()) 
    if not options.no_scramble_octaves: 
        _dict["octaves"] = sorted(_dict["octaves"], key = lambda x: random.random())
    return _dict

def create_chord(_dict):
    _dict["chord"] = []
    for i in range(0, len(_dict["notes"])-1):
        string = "%s%s" % (_dict["notes"][i], _dict["octaves"][i])
        if find_element(_dict["chord"], string) == -1:
            _dict["chord"].append(string)

    _dict["chord"] = chord.Chord(_dict["chord"])
    return _dict
    
def glitch(aStream, options):
    """ Esta secao vai selecionar alguns trechos da peca:
    - extrair arcordes das notas usadas em cada bloco
    - embaralhar a ordem vertical dos acordes
    - sequenciar estes acorde na sua ordem ritmica normal
    - apos isso, o compositor deve verificar a ordem dos intervalos  livremente, organizando assim uma CAC. 
    """
    newStream = stream.Stream()
    if aStream.metadata is not None:
        print("%s, %s" % (aStream.metadata.composer, aStream.metadata.title))
    # Extrai as partes do stream original
    for part in aStream.parts:
        
        print("=======================\n%s" % part.id)

        # Escolhe randomicamente uma secao da peca para ser modificado
        measures = choice_measures(part)

        # Criar acordes a partir das notas dadas
        _dict = {}
        for m in measures:
            _dict = verify_and_map_notes_in_measure(m)
            _dict = scramble_notes_if(_dict, options)
            _dict = create_chord(_dict)

            print(_dict["chord"])
      
            # Escolher:
            # 5: bordadura 
            # 6: arpejo
            # Aplica erros randomicos
            r = rnd(float(options.glitch))

            # 0: posicao fechada
            if r == 0:
                newStream.append(_dict["chord"].closedPosition())

            # 1: posicao semi fechada
            elif r == 1:
                newStream.append(_dict["chord"].semiClosedPosition())

            # 2: posicao superaberta
            elif r == 2:
                _octaves = range(1, len(_dict["notes"])-1)
                _chord = map(lambda i: "%s%s" % (_dict["notes"][i], i+1), _octaves) 
                newStream.append(chord.Chord(_chord))
                
            # 3: Separa uma nota do acorde
            elif r == 3:
                _stream = stream.Stream()

                _pitch = pitch.Pitch(_dict["chord"].pitches[0])
                _dur = duration.Duration(0.5)
                _note = note.Note(_pitch, _dur)
                _dur2 = duration.Duration(0.5)
                _chord = chord.Chord([_dict["chord"].pitches[i] for i in range(1,len(_dict["chord"].pitches)-1)], duration=_dur2)
                
                newStream.append(_note)
                newStream.append(_chord)
            
            ###
            # 4: Separa duas notas do acorde
            elif r == 4:
                _stream = stream.Stream()
                _p = _dict["chord"].pitches
                lp = len(p)

                for i in range(2):
                    dur = duration.Duration(1.0/rnd(lp))
                    _notes.append(note.Note(_p[i], dur))
                
                dur0 = _durs[0].quarterLength
                dur1 = _durs[1].quarterLength
                                  
                _rest = 1 - (dur0 + dur1)
                _dur = duration.Duration(_rest)
                
                _chord = chord.Chord([_dict["chord"].pitches[i] for i in range(2,len(_dict["chord"])-2)], duration=_dur)
                
                newStream.append(_notes)
                newStream.append(_chord)
            elif r == 5:
                _stream = stream.Stream()
                __durs = []

                __durs = [1/(i+2) for i in range(len(c.pitches))]

                #print __durs
                _rndindex = int(rnd(len(__durs)))
                #print _rndindex
                #print __durs[_rndindex]
                    
                _durs = [duration.Duration(__durs[_rndindex]) for i in [0,1,2]]

                _notes = []
                if(len(c.pitches) > 3):
                    _notes = [note.Note(c.pitches[i], _durs[i]) for i in [0,1,2]]
                else:
                    if(len(c.pitches) > 2):
                        _notes = [note.Note(c.pitches[i], _durs[i]) for i in [0,1]]
                        _notes.append(note.Note(c.pitches[0]))
                    else:
                        if(len(c.pitches > 0)):
                            _notes = [note.Note(c.pitches[0])]
                        else:
                            _notes = [note.Rest()]


                _rest = 1-(_durs[0].quarterLength+_durs[1].quarterLength+_durs[2].quarterLength)
                _dur = duration.Duration(_rest)
                _chord = chord.Chord([c.pitches[i] for i in range(3,len(c)-3)], duration=_dur)
                
                newStream.append(_notes)
                newStream.append(_chord)
    # retorna o novo stream
    return newStream



def find_element(p,t):
    """Funcao de ajuda
    http://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python
    """
    i = 0
    for e in p:
      if e == t:
          return i
      else:
          i +=1
        
    return -1

def search_only(options):
    print("m21> searching...")
    metadata = search_stream(options)
    datas = [data.sourcePath for data in metadata]
    return datas

def ordered_pitch_interval(notes):
    _result = []
    for i in range(len(notes)):
            for j in range(len(notes[i])):
                _interval = None
                if(not j == len(notes[i])-1):
                    _interval = interval.notesToChromatic(notes[i][j], notes[i][j+1])
                    _result.append(_interval.semitones)
                else:
                    if(not i == len(notes)-1):
                        _interval = interval.notesToChromatic(notes[i][len(notes[i])-1], notes[i+1][0])
                        _result.append(_interval.semitones)
    #_result.pop(len(_result)-1)
    return _result

def unordered_pitch_interval(notes):
    _result = ordered_pitch_interval(notes)
    _result = map((lambda x: abs(x)), _result)
    return _result

def ordered_pitch_class_interval(notes):
    _result = ordered_pitch_interval(notes)
    _result = map((lambda x: (12 - x) % 12), _result)
    return _result

def get(options):
    """Captura um stream qualquer"""
    if(options.xml):
        return converter.parse(options.xml)
    elif(options.tinynotation):
        return converter.parse(options.tinynotation, format="tinynotation")
    elif(options.composer and options.index):
        c = "%s/%s" % (options.composer, options.index)
        return corpus.parse(c)

def plot(_stream, t):
    """Analisa categorias de alturas de um stream qualquer e plota em um grafico, abrido um aplicativo de imagens (eog, padrao); para modificar qual programa vai abrir ver ~/.music21rc"""
    try:
        if t == "PlotStream":
            graph.plotStream(_stream)
        if(_stream.classes[0] is 'Score'):
            for _part in _stream.parts:
                graph.plotStream(_part, t)
        else:
            graph.plotStream(_stream, t)
    except Exception as e:
        print("m21> %s: %s" % (e, _stream))
        exit

def show(_stream, options):
    print(_stream)
    if((type(_stream) is not None) and _stream.classes[0] is 'Part'):
        now = datetime.datetime.now()
        _s = stream.Stream()
        _metadata = metadata.Metadata(title=options.title, composer=options.author, date=("%d/%d/%d" % (now.day,now.month,now.year)))
        _metadata.composer = "%s (generated at %s)" % (_metadata.composer, _metadata.date)
        _s.insert(_metadata)
        _s.append(_stream)
        _s.show()
    else:
        _stream.show()
   

def invert_and_or_transpose(_stream, options):
    """Inverte ou transpoe um stream"""
    _intervals = _stream.findConsecutiveNotes(skipRests=True)
    s = stream.Score()
    s.append(_intervals)
    s.show('text')

def select_measures(_stream, options):
    """Seleciona compassos de um stream"""
    return  _stream.measures(int(options.measures[0]), int(options.measures[1]))

def reducte_piano(_stream, options):
    """Retorna uma reducao de acordes"""
    _chords = _stream.chordify()
    #_stream.insert(0, _chords)
    for c in _chords.flat:
        if 'Chord' not in c.classes:
            continue
        c.closedPosition(forceOctave=4, inPlace=True)
        if options.tonal_harmonic_analysis:
            rn = roman.romanNumeralFromChord(c, key.Key(options.tonal_harmonic_analysis))
            c.addLyric(str(rn.figure))

    return _chords
    
