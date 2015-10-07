%=============================================
%   created by MuseScore Version: 1.3
%          sexta-feira, 10 de julho de 2015
%=============================================

\version "2.12.0"



#(set-default-paper-size "a5")

\paper {
  line-width    = 120\mm
  right-margin  = 15\mm
  left-margin   = 15\mm
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
    \time 6/8 
    <c d a' bes>4 \clef "treble^8"
    \arpeggioArrowUp <f' bes'>\arpeggio  a,      | % 1
    <d bes'>8 <d e f g>4 <a bes c d> r8      | % 2
    r <fis a bes d> r4 <c' d bes'>8 r      | % 3
    r <f bes> g4 <cis, d f>8 <d e>~      | % 4
    <d e> r2 \clef bass
    \arpeggioArrowUp <fis,, d'>8 ~      | % 5
    <fis d'> \clef treble
    <f' g>4 bes <bes, c>8~\mf     | % 6
    <bes c> r4 <d d'>\arpeggio  r8      | % 7
    r <bes' g'>4 r4.      | % 8
    r2 r4      | % 9
    <g, a bes> <c c'>\arpeggio  \clef bass
    a8 g~      | % 10
    g r4. <f g>4      | % 11
    a <fis g bes>2      | \bar "|." 
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
    \time 6/8 
    r4\fff\> \arpeggioArrowDown <ais c>  d \clef treble
         | % 1
    <d' c'>8 \clef bass
    r d,,4\!\mp  r8 c'~\ff\>     | % 2
    c r ais4 a      | % 3
    d,8 e4 r8 r4      | % 4
    r8 \arpeggioNormal <d' e f fis>4\arpeggio  d,\!\p fis8\f\>      | % 5
    fis r \arpeggioArrowDown<f f'>4\arpeggio  d\pp      | % 6
    r8 a''4\> r8 <dis,, c'> <g' a>~      | % 7
    <g a> r <e, f'>\arpeggio  <cis' e f>4 g8~      | % 8
    g d'\!\p f4 <c d ees>\mf      | % 9
    r\> <ais ais'>\arpeggio  <cis e f>      | % 10
    f8 a,4 dis, <c' d>8~      | % 11
    c d4\pp g,4.         |  \bar "|." 
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

#(set-global-staff-size 20)
