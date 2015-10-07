%=============================================
%   created by MuseScore Version: 1.3
%          domingo, 26 de julho de 2015
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
title = "Coral #145"
composer = "Bach / music21"
subtitle = "Após extração fragmentada do BWV12 em 26/07/15"
dedication = "saudades da Larissa Pereira"
arranger = "Guilherme Lunhani"
copyright = "cc-by-sa 4.0"
}

AvoiceAA = \relative c{
    \set Staff.instrumentName = #""
    \set Staff.shortInstrumentName = #""
    \clef bass
    %staffkeysig
    \key c \major 
    %bartimesig: 
    \time 4/4 
    d'1~ \ff      | % 1
    d\fermata       | % 2
    R1  | % 
    r2 gis,4 \p b~      | % 4
    b1\fermata       | % 5
    R1  | % 
    fis4 \mf <g a>8 <b cis>4 e4.\fermata       | % 7
    R1 *3  | % 
    \clef treble
         | % 10
    bes2~ bes      | % 11
    R1  | % 
    fis'1      | % 13
    R1  | % 
    <b' d>1      | % 15
    R1  | % 
    fis,1      | % 17
    R1  | % 
    r2 bes,\fermata      | % 19
    R1  | % 
    r2. \clef bass
    fis4      | % 21
    <g a>8 <b cis>4 e2 b8~      | % 22
    b1 \mp      | % 23
    gis \p\fermata      | % 24
    R1  | % 
    d'1~      | % 26
    d      | % 27
    R1 \bar "|." 
}% end of last bar in partorvoice

 
AvoiceAB = \relative c{
    s1 s1 s1 s1 s1 s1 s1 s1 s1 s1  | % 
    r2 a'''\fermata       | % 11
    s1      | % 12
    s1      | % 13
    s1      | % 14
    s1      | % 15
    s1      | % 16
    s1      | % 17
    s1      | % 18
    a1      | % 19
    s1      | % 20
    s1      | % 21
    s1      | % 22
    s1      | % 23
    s1      | % 24
    s1      | % 25
    s1      | % 26
    s1      | % 27
    s1 \bar "|." 
}% end of last bar in partorvoice

 
ApartA =  << 
    \mergeDifferentlyHeadedOn
    \mergeDifferentlyDottedOn 
        \context Voice = AvoiceAA\AvoiceAA\\ 
        \context Voice = AvoiceAB\AvoiceAB
        >> 

 

AvoiceBA = \relative c{
    \set Staff.instrumentName = #""
    \set Staff.shortInstrumentName = #""
    \clef bass
    %staffkeysig
    \key c \major 
    %bartimesig: 
    \time 4/4 
    r2 <d cis'>4 \p g~     | % 1
    g1_\fermata       | % 2
    R1  | % 
    a1~ \ff      | % 4
    a\fermata       | % 5
    R1 *3  | % 
    bes8 a,4 <bis cis d fis> gis4._\fermata       | % 9
    R1  | % 
    r4 \ff r \p g'2      | % 11
    R1  | % 
    <g, d'>1 \mp      | % 13
    R1  | % 
    a,1      | % 15
    R1  | % 
    <g' d'>1      | % 17
    R1 \ff  | % 
    g'1      | % 19
    R1  | % 
    gis,4. \p ais'8 a,4 \< <bis cis d fis>~      | % 21
    <bis cis d fis>1 \! \ff      | % 22
    R1 *3  | % 
    g'1~ \ff      | % 26
    g     | % 27
    R1 \bar "|." 
}% end of last bar in partorvoice

 
AvoiceBB = \relative c{
    s1 s1 s1  | % 
    r2. a4~ \p      | % 4
    a1_\fermata       | % 5
    s1      | % 6
    s1      | % 7
    s1      | % 8
    s1      | % 9
    s1      | % 10
    r4 b~ b2_\fermata       | % 11
    s1      | % 12
    s1      | % 13
    s1      | % 14
    s1      | % 15
    s1      | % 16
    s1      | % 17
    s1      | % 18
    r4 b2. \p \fermata     | % 19
    s1      | % 20
    s1      | % 21
    s1      | % 22
    s1      | % 23
    s1      | % 24
    R1  | % 
    r2 <d cis'>~ \p      | % 26
    <d cis'>1      | % 27
    s1 \bar "|." 
}% end of last bar in partorvoice

 
ApartB =  << 
    \mergeDifferentlyHeadedOn
    \mergeDifferentlyDottedOn 
        \context Voice = AvoiceBA\AvoiceBA\\ 
        \context Voice = AvoiceBB\AvoiceBB
        >> 


\score { 
    << 
        \context PianoStaff <<
        \set PianoStaff.instrumentName="Piano" 
            \context Staff = ApartA << 
                \ApartA
                \set Staff.instrumentName = #""
                \set Staff.shortInstrumentName = #""
            >>

            \context Staff = ApartB << 
                \ApartB
                \set Staff.instrumentName = #""
                \set Staff.shortInstrumentName = #""
            >>
        >> %end of PianoStaffA
  >>

}%% end of score-block 

#(set-global-staff-size 20)
