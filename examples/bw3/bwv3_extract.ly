%=============================================
%   created by MuseScore Version: 1.3
%          quinta-feira, 9 de julho de 2015
%=============================================

\version "2.12.0"



#(set-default-paper-size "a5")

\paper {
  line-width    = 120\mm
  left-margin   = 15\mm
  right-margin = 15\mm
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
    <b, fis' gis' a'>4 <fis''' gis a b> <fis gis a b> <cis,,, cis' cis' b''>      | % 1
    <cis''' d a'> <cis,,, b'' a'> <gis'''' a> <dis,,, b'' dis>      | % 2
    <dis''' e fis> <e fis gis b> <a,,, gis' a' e' cis'> <fis a' b' gis'>      | % 3
    <cis'' dis gis a b> <b, e a' b'> <cis'' d e fis gis> <cis e gis a>     | % 4
    <e, fis gis a>4 <e, b'> <cis' d e fis gis a> \bar "|." 
}% end of last bar in partorvoice


\score { 
    << 
        \context Staff = ApartA << 
            \context Voice = AvoiceAA \AvoiceAA
        >>
    >>
}%% end of score-block 

#(set-global-staff-size 20)
