%=============================================
%   created by MuseScore Version: 1.3
%          sexta-feira, 10 de julho de 2015
%=============================================

\version "2.12.0"



#(set-default-paper-size "a5")

\paper {
  line-width    = 120\mm
  right-margin = 15\mm
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
    \time 4/4 
    <b d>16 e8 b'2.~ b16\fermata       | % 1
    r b, e b'2.~ b16\fermata       | % 2
    R1  | % 
    %bartimesig: 
    \time 2/2 
    d,2 e      | % 4
    e fis      | % 5
    e fis\fermata       | % 6
    r1      | % 7
    %bartimesig: 
    \time 4/4 
    <d dis e fis>16~ \f <b e fis>2. <b e fis>16-|  r8      | % 8
    r1 \fermata      | % 9
    %bartimesig: 
    \time 2/2 
    r1 \fermata      | % 10
    <a b>8~ ^\markup {\upright  ""} <a b d>2 r4. \fermata      | % 11
    %bartimesig: 
    \time 2/2 
    r1      | % 12
    r2 a' \clef bass
         | % 13
    <c,, g' a>16 <ais b cis> <e' fis> r2. r16      | % 14
    <e fis>-|  \ff r8. r2. \bar "|." 
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
    d,1\fermata  \> \f      | % 1
    b'16 \! \mf e r <d, d'>2.~ \> <d d'>16\fermata       | % 2
    R1 \!  | % 
    %bartimesig: 
    \time 2/2 
    r1 \p      | % 4
    r      | % 5
    r      | % 6
    r \fermata      | % 7
    %bartimesig: 
    \time 4/4 
    r16 ais''2.~ ais8.~      | % 8
    ais2 r \fermata      | % 9
    %bartimesig: 
    \time 2/2 
    ais2 \p ais\fermata       | % 10
    <c, g'>16 \mf fis~ <b, cis fis>2 \< r4. \fermata      | % 11
    %bartimesig: 
    \time 2/2 
    fis'2 \! ais \<      | % 12
    a \! b      | % 13
    r16 \< <e,, fis> r <fis dis'>2.~ <fis dis'>16~ \f      | % 14
    <fis dis'>1 \!      |  \bar "|." 
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
