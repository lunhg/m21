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
    \time 2/4 
    a'16 b a <e fis>4 r16      | % 1
    <ais cis>8. b8. r8      | % 2
    dis,16 b' dis, e r <fis a b>8.~      | % 3
    <fis a b>16 r8. fis8. <d fis>16~      | % 4
    <d fis>8. r8 dis16 fis d'      | % 5
    e, fis d r r b a' b,      | % 6
    a' r <c, g'>8. cis8 <ais' b>16~      | % 7
    <ais b>8. <a, b>8. <c g'>8~      | % 8
    <c g'>16 r r8 r16 b'8.      | % 9
    <d, g b>16 d8. r8. <c' d g a>16~      | % 10
    <c d g a>8. r8. <c g' b>8~      | % 11
    <c g' b> r \clef bass
    <b,, cis>4      | % 12
    r16 b'8. <e, fis>8. <a, b>16~      | % 13
    <a b>8. <ais b cis>16~ <ais b cis>4~      | % 14
    <ais b cis>2      |\bar "|." 
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
    \time 2/4 
    R2  | % 
    <d' e>8. <cis d>8. e,,8~      | % 2
    e4 d      | % 3
    r16 d4. r16      | % 4
    r dis4. r16      | % 5
    r dis4. r16      | % 6
    r8 d'8. r8.      | % 7
    <fis b>8. <c g'>8. <c g'>8~      | % 8
    <c g'>16 r fis g fis8. <c b'>16~      | % 9
    <c b'>8 <e, cis'>8. <g fis'>8.      | % 10
    r8. a8. r16 r      | % 11
    r gis' b gis <d, e ais>4      | % 12
    r16 dis8. r8. <c e>16~      | % 13
    <c e>8. <d e>16~ <d e>4~      | % 14
    <d e>2      |  \bar "|." 
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
