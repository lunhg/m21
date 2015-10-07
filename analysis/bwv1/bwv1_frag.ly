%=============================================
%   created by MuseScore Version: 1.3
%          quinta-feira, 23 de julho de 2015
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

AvoiceAA = \relative c'{
    \set Staff.instrumentName = #"Horn 2"
    \set Staff.shortInstrumentName = #""
    \clef treble
    %staffkeysig
    \key f \major 
    %barkeysig: 
    \key f \major 
    %bartimesig: 
    \time 4/4 
    \partial 4*1
    f4      | % 1
    g8 c, f f, a f a c      | % 2
    f16 bes a g f8 g a4 a      | % 3
    f8 g16 a bes8 c16 bes a8 g g c      | % 4
    c b16 a b4 c f, \bar "|." 
}% end of last bar in partorvoice

 

AvoiceBA = \relative c'{
    \set Staff.instrumentName = #"Soprano"
    \set Staff.shortInstrumentName = #""
    \clef treble
    %staffkeysig
    \key f \major 
    %barkeysig: 
    \key f \major 
    %bartimesig: 
    \time 4/4 
    \partial 4*1
    f4      | % 1
    c' a f c'      | % 2
    d d c c      | % 3
    d e f e      | % 4
    d d c a \bar "|." 
}% end of last bar in partorvoice

 

AvoiceCA = \relative c'{
    \set Staff.instrumentName = #"Alto"
    \set Staff.shortInstrumentName = #""
    \clef treble
    %staffkeysig
    \key f \major 
    %barkeysig: 
    \key f \major 
    %bartimesig: 
    \time 4/4 
    \partial 4*1
    c4      | % 1
    c c d f      | % 2
    bes bes a a      | % 3
    bes bes c8 d c g      | % 4
    a4 g g f \bar "|." 
}% end of last bar in partorvoice

 

AvoiceDA = \relative c{
    \set Staff.instrumentName = #"Tenor"
    \set Staff.shortInstrumentName = #""
    \clef "treble_8"
    %staffkeysig
    \key f \major 
    %barkeysig: 
    \key f \major 
    %bartimesig: 
    \time 4/4 
    \partial 4*1
    a'4      | % 1
    g a a a      | % 2
    f f' f f      | % 3
    f g f8 d e4      | % 4
    f8 e d4 e c8 a \bar "|." 
}% end of last bar in partorvoice

 

AvoiceEA = \relative c{
    \set Staff.instrumentName = #"Bass"
    \set Staff.shortInstrumentName = #""
    \clef bass
    %staffkeysig
    \key f \major 
    %barkeysig: 
    \key f \major 
    %bartimesig: 
    \time 4/4 
    \partial 4*1
    f4      | % 1
    e f d a      | % 2
    bes8 c d e f4 f      | % 3
    bes a8 g a b c4      | % 4
    f, g c, f \bar "|." 
}% end of last bar in partorvoice


\score { 
    << 
        \context Staff = ApartA << 
            \context Voice = AvoiceAA \AvoiceAA
        >>


        \context Staff = ApartB << 
            \context Voice = AvoiceBA \AvoiceBA
        >>


        \context Staff = ApartC << 
            \context Voice = AvoiceCA \AvoiceCA
        >>


        \context Staff = ApartD << 
            \context Voice = AvoiceDA \AvoiceDA
        >>


        \context Staff = ApartE << 
            \context Voice = AvoiceEA \AvoiceEA
        >>




      \set Score.skipBars = ##t
      %%\set Score.melismaBusyProperties = #'()
      \override Score.BarNumber #'break-visibility = #end-of-line-invisible %%every bar is numbered.!!!
      %% remove previous line to get barnumbers only at beginning of system.
       #(set-accidental-style 'modern-cautionary)
      \set Score.markFormatter = #format-mark-box-letters %%boxed rehearsal-marks
       \override Score.TimeSignature #'style = #'() %%makes timesigs always numerical
      %% remove previous line to get cut-time/alla breve or common time 
      \set Score.pedalSustainStyle = #'mixed 
       %% make spanners comprise the note it end on, so that there is no doubt that this note is included.
       \override Score.TrillSpanner #'(bound-details right padding) = #-2
      \override Score.TextSpanner #'(bound-details right padding) = #-1
      %% Lilypond's normal textspanners are too weak:  
      \override Score.TextSpanner #'dash-period = #1
      \override Score.TextSpanner #'dash-fraction = #0.5
      %% lilypond chordname font, like mscore jazzfont, is both far too big and extremely ugly (olagunde@start.no):
      \override Score.ChordName #'font-family = #'roman 
      \override Score.ChordName #'font-size =#0 
      %% In my experience the normal thing in printed scores is maj7 and not the triangle. (olagunde):
      \set Score.majorSevenSymbol = \markup {maj7}
  >>

  %% Boosey and Hawkes, and Peters, have barlines spanning all staff-groups in a score,
  %% Eulenburg and Philharmonia, like Lilypond, have no barlines between staffgroups.
  %% If you want the Eulenburg/Lilypond style, comment out the following line:
  \layout {\context {\Score \consists Span_bar_engraver}}
}%% end of score-block 

#(set-global-staff-size 14)
