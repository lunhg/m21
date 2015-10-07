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
    title = "Music21 Fragment"
    composer = "Music21"
    }

AvoiceAA = \relative c{
    \set Staff.instrumentName = #""
    \set Staff.shortInstrumentName = #""
    \clef treble
    %staffkeysig
    \key c \major 
    %bartimesig: 
    \time 4/4 
    <c' g'>4 <f g a> <c f a bes bes'> <c a' c>      | % 1
    <c' d> <c, d f> <a' bes> <c, d g bes>      | % 2
    <f g> <g, a> f <e' f g>      | % 3
    \clef bass
    <e, f a c d> <f g a> <g a bes> <f, c' d e bes'>      | % 4
    <c' g' a bes> <c f g> <e, c' d bes'> <c' f>      | % 5
    <e, f' a> <d' e f bes> <c g' a bes b'> <c f g>      | % 6
    <d, c' e f>4 \bar "|." 
}% end of last bar in partorvoice

\score { 
    << 
        \context Staff = ApartA << 
            \context Voice = AvoiceAA \AvoiceAA
        >>
    >>
}%% end of score-block 

#(set-global-staff-size 20)
