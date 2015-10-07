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
    title = "False"
    composer = "False (generated at 0023/07/2015)"
}

AvoiceAA = \relative c'{
    \set Staff.instrumentName = #""
    \set Staff.shortInstrumentName = #""
    \clef treble
    %staffkeysig
    \key f \major 
    %barkeysig: 
    \key f \major 
    %bartimesig: 
    \time 4/4 
    \partial 4*1
    <f a c>4      | % 1
    <e g c>8 <e g c> <f a c> <f a c> <d f a> <d f a> <a' c f> <a c f>      | % 2
    <bes d f>16 <bes d f> <c, d f a bes> <c d f g bes> <d f bes>8 <e f g bes d> <f a c>4 <f a c>      | % 3
    <bes d f>8 <bes d f g>16 <bes d f a> <a bes e g>8 <g bes c e>16 <g bes e> <a c f>8 <b d f g> <c, e g> <c e g>      | % 4
    <f a c d> <f a b d e>16 <f a d e> <g b d>4 <c, e g> <f a c>8 <f a> \bar "|." 
}% end of last bar in partorvoice

      ApartAverseA = \lyricmode { \set stanza = "F: " I "V6" "V6" I I vi vi "I6" "I6" IV IV "IV7642" "ii754#2" "IV6" "viio#7532" I I IV "ii65#3" "IV7" "viio7#52" "V43" "viio#63" "I6" "II65" V V "vi#65#3" "#ivo7643" "vi#7#6#3" II V I I }

\score { 
    << 
        \context Staff = ApartA << 
            \context Voice = AvoiceAA \AvoiceAA
        >>

         \context Lyrics = ApartAverseA\lyricsto AvoiceAA  \ApartAverseA



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

#(set-global-staff-size 20)
