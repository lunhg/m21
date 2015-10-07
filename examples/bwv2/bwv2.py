# Coral randomico
from music21 import *
import math, random

aStream = corpus.parse('bach/bwv2')
aStream.show()

# Esta secao vai selecionar alguns trechos da peca,
# extrair arcordes das notas usadas em cada bloco
# embaralhar a ordem vertical dos acordes
# e sequenciar estes acorde na sua ordem ritmica normal
# apos isso, o compositor deve verificar a ordem dos intervalos
# livremente, organizando assim uma CAC. 
newStream = stream.Stream()

# Funcao de ajuda
# http://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python
def find_element(p,t):
  i = 0
  for e in p:
    if e == t:
      return i
    else:
      i +=1
  
  return -1

# Extrai as partes
for part in aStream.parts:
  print "%s" % part.id

  # Escolhe randomicamente uma secao da peca para ser modificada
  r = [int(math.floor(random.random() * len(part.measureOffsetMap()))) for i in [0, 1]]
  a = min(r[0], r[1])
  b = max(r[0], r[1])

  if(not b>a):
    b = a + 1

  print "-----------------------\nmeasures: %d:%d" % (a, b)
  matrix = [measure for measure in part.measures(a, b)]
  #print "  %s" % str(matrix)

  measures = [matrix[i] for i in range(4,len(matrix))]

  # Criar acordes a partir das notas dadas
  for m in measures:
    notes = [str(p.name) for p in m.notes]
    octaves = [str(p.octave) for p in m.notes]
    scramble_notes = sorted(notes, key = lambda x: random.random())
    scramble_octaves = sorted(octaves, key = lambda x: random.random())
    
    #print "%s: \n    normal:    %s\n    scrambled: %s" % (m.notes, notes, scramble_notes)
    #print "    normal:     %s\n    scrambled: %s" % (octaves, scramble_octaves)

    aij = []
    for i in range(0, len(notes)-1):
      string = "%s%s" % (scramble_notes[i], scramble_octaves[i])
      if find_element(aij, string) == -1:
        aij.append(string)

    if(len(aij) > 0):
      c = chord.Chord(aij)
      print c
      
      # Escolher:
      # 0: posicao fechada
      # 1: posicao semi fechada
      # 2: posicao superaberta
      r = math.floor(random.random() * 3)
      if r == 0:
        c = c.closedPosition()
      elif r == 1:
        c = c.semiClosedPosition()
      elif r == 2:
        _octaves = range(0, len(scramble_notes)-1)
        _chord = [""+str(scramble_notes[i])+""+str(i+1) for i in _octaves]
        c = chord.Chord(_chord)
        

      newStream.append(c)

# Abrir no musescore (exportar depois para lilypond)
newStream.show()
