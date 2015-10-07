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
    title = "Music21 Fragment"
    composer = "Music21"
    }

AvoiceAA = \relative c{
    \set Staff.instrumentName = #""
    \set Staff.shortInstrumentName = #""
    \clef bass
    %staffkeysig
    \key c \major 
    %bartimesig: 
    \time 4/4 
    \partial 4*3
    a''4 b a      | % 1
    <e fis> <d e ais cis> <cis d b'> e,,      | % 2
    dis'' b' dis,      | % 3
    e d <fis a b>      | % 4
    d fis <d fis>      | % 5
    dis fis dis      | % 6
    e fis d      | % 7
    dis,, b'' a b      | % 8
    a <d, c' g'>8 cis'4 <ais' b>8      | % 9
    <fis, b>4 <c g' a b> fis g      | % 10
    fis b' <c,, b'>8 <d g b>~      | % 11
    <d g b> <e, cis' d'>4 <g fis'> <c d g a> a8~      | % 12
    a <c g' b>4 gis' b gis8~      | % 13
    gis <d, e ais b cis>4 <dis b''> <e' fis>8~      | % 14
    <e fis> <c, e a b>4 <d e ais b cis> \bar "|." 
}% end of last bar in partorvoice


\score { 
    << 
        \context Staff = ApartA << 
            \context Voice = AvoiceAA \AvoiceAA
        >>
  >>
}%% end of score-block 

#(set-global-staff-size 20)
