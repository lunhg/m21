%=============================================
%   created by MuseScore Version: 1.3
%          quarta-feira, 8 de julho de 2015
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
title = "Coral #1"
subtitle = "Após uma extração de alturas do BWV1 em 08/7/2015"
composer = "Bach / music21"
dedication = "para Glerm Soares"
arranger = "Guilherme Lunhani"
copyright = "cc-by-sa 4.0"
}

AvoiceAA = \relative c'{
    \set Staff.instrumentName = #""
    \set Staff.shortInstrumentName = #""
    \clef treble
    %staffkeysig
    \key c \major 
    %barkeysig: 
    \key c \major 
    %bartimesig: 
    \time 4/4 
    \mark \markup { \italic {Largo} }
    g'4 <g a> <b bes'> <a c>      | % 1
    <c d>2.\fermata  <a bes>4~(      | % 2
    <g bes> <f g>2) r4      | % 3
    r2. <e f g>4 \clef bass
         | % 4
    <c d>2 r4 <d, e bes'>~      | % 5
    <d e bes'>2.\fermata  <a' bes>4      | % 6
    <c, bes'>2.\fermata f4~      | % 7
    <f a>1\fermata       | % 8
    R1  | % 
    <e bes'>4\pp \clef treble
    <bes' b'>2 \clef bass
    <e, f>4~\sfz      | % 10
    <e f>1      | % 12
    r1
}% end of last bar in partorvoice

 

AvoiceBA = \relative c{
    \set Staff.instrumentName = #""
    \set Staff.shortInstrumentName = #""
    \clef bass
    %staffkeysig
    \key c \major 
    %barkeysig: 
    \key c \major 
    %bartimesig: 
    \time 4/4 
    c'4 \f f\< <c f a> c      | % 1
    r2.\!\ff <c d f>4~(      | % 2
    <c d f> \> <c d>2 <g a>4      | % 3
    f2.\fermata\!\p) r4\f      | % 4
    <e f a>(\< <f g a> <g a bes>) <f, c'>~\!\ff      | % 5
    <f c'>2.\fermata <c' f g>4      | % 6
    <e, d'>2.\fermata r4\sfz      | % 7
    e1\mp\fermata       | % 8
    r1  | %
    r	   |
    <d' f>4( \f <c g' a>\> <c f g>) <d, c'>~\!\mf    | % 11
    <d c'>2.\fermata  r4      | % 12
    \bar "|." 
}% end of last bar in partorvoice


\score { 
    << 
        \context PianoStaff <<
        \set PianoStaff.instrumentName="Piano" 
            \context Staff = ApartA << 
                \context Voice = AvoiceAA \AvoiceAA
                \set Staff.instrumentName = #""
                \set Staff.shortInstrumentName = #""
            >>


            \context Staff = ApartB << 
                \context Voice = AvoiceBA \AvoiceBA
                \set Staff.instrumentName = #""
                \set Staff.shortInstrumentName = #""
            >>


        >> %end of PianoStaffA
    >>
}%% end of score-block 