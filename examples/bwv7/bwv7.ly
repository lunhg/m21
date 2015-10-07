%=============================================
%   created by MuseScore Version: 1.3
%          quarta-feira, 29 de julho de 2015
%=============================================

\version "2.12.0"

#(set-default-paper-size "a5")

\paper {
  line-width    = 125\mm
  left-margin   = 10\mm
  top-margin    = 10\mm
  bottom-margin = 20\mm
  %%indent = 0 \mm 
  %%set to ##t if your score is less than one page: 
  ragged-last-bottom = ##t 
  ragged-bottom = ##f  
  %% in orchestral scores you probably want the two bold slashes 
  %% separating the systems: so uncomment the following line: 
  %% system-separator-markup = \slashSeparator 
}

\header {
title = "Coral #7"
composer = "Bach / music21"
subtitle = "Após extração fragmentada do BWV7 em 29/07/15"
dedication = "x"
arranger = "Guilherme Lunhani"
copyright = "cc-by-sa 4.0"
}

AvoiceAA = \relative c'{
    \set Staff.instrumentName = #""
    \set Staff.shortInstrumentName = #""
    \clef treble
    %staffkeysig
    \key c \major 
    %bartimesig: 
    \time 2/2 
    \times 2/3{r4 ^\markup {\upright \bold  "Largo"} cis'8  } \clef bass
    <d,, a' c>2.~      | % 1
    <d a' c>1\fermata       | % 2
    r2 \clef treble
    r8 \times 2/3{r16 e' e'  } \times 2/3{e' fis d,~  } d8~      | % 3
    d2.\fermata  r4      | % 4
    b,16 r8. <fis' g a b>2.~ \fff      | % 5
    <fis g a b>2.\fermata  \times 2/3{g4 g'8  }      | % 6
    r4 <fis, ais>2\fermata  \sfz <dis e fis g>4~      | % 7
    \times 2/3{<dis e fis g>4 <dis e fis g>8  } b''2 \p d,,4~      | % 8
    <d d'>2\fermata  r      | % 9
    r <g e'>\trill  \clef bass
         | % 10
    r4 \clef treble
    \times 2/3{fis4 g' fis' d e, fis' r8  } <g,, a b>2 \clef bass
         | % 11
    r4 \p <e, fis g b>16 <e fis g b>8.~ b'2      | % 12
    b,1      | % 13
    b'      | % 14
    r      | % 15
    <cis, d e>2 \clef treble
    <fis' e'> \clef bass
         | % 16
    \times 2/3{<fis, a b>4 r e r cis \clef "treble^8"
    r a'''16 r8  } r4 \clef bass
    r2 \mf      | % 17
    \times 2/3{d,,,4 \< r a' r b r fis r \clef treble
    fis''8  } r4 a,2\trill  \bar "|."     | % 18
    a'1\fermata  \! \bar "|." 
}% end of last bar in partorvoice

 

AvoiceBA = \relative c'{
    \set Staff.instrumentName = #""
    \set Staff.shortInstrumentName = #""
    \clef treble
    %staffkeysig
    \key c \major 
    %bartimesig: 
    \time 2/2 
    r1 \mf      | % 1
    r4 e2\trill  \mp fis4 \clef bass
         | % 2
    <ais,, b'>2\fermata  \sfz r \mp \clef treble
         | % 3
    r8. <cis' cis'>2.\fermata  \f \clef bass
    r16      | % 4
    cis, \ff r8. r4 r2      | % 5
    \grace{\stemUp b16  } \stemNeutral cis2\trill  dis4\fermata  r      | % 6
    e,2. cis4~ \f      | % 7
    cis2 d4 \< \f cis'~      | % 8
    cis2\fermata  \! r      | % 9
    r r4 \p <a e'>~\trill       | % 10
    <a e'> <fis fis'> \< <fis' b dis e>2 \f      | % 11
    fis,1 \! \ff      | % 12
    a \fff      | % 13
    e \p      | % 14
    r      | % 15
    r2 \p <fis g'>      | % 16
    \times 2/3{r4 \mf e r fis r \clef treble
    b'' r g''8 \clef bass
    r4 <e,,,, fis b>16 <e fis b>4 r8 r16      | % 17
    r4 \mf g' r e, r g r \clef treble
    b' r8 \clef bass
    r4 <e,, d'>16 \f <e d'>4 \bar "|."     | % 18
    r4 \p g\prall  a2\fermata  \bar "|." 
}% end of last bar in partorvoice


\score { 
    

}%% end of score-block 

#(set-global-staff-size 20)
