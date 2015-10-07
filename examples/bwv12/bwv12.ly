%=============================================
%   created by MuseScore Version: 1.3
%          quarta-feira, 22 de julho de 2015
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
title = "Coral #12"
composer = "Bach / music21"
subtitle = "Após extração fragmentada do BWV12 em 22/07/15"
dedication = "para Fábio Menezes Evangelista"
arranger = "Guilherme Lunhani"
copyright = "cc-by-sa 4.0"
}

APnovoiceAA = \relative c'{
    \set Staff.instrumentName = #"Piano"
    \set Staff.shortInstrumentName = #"Pno."
    \clef treble
    %staffkeysig
    \key c \major 
    %bartimesig: 
    \time 3/16 
    \partial 16*3
    \mark  \markup {\italic "Vivo"}
    
    %%% Parte A
    d'16[\( g d]     | % 1
    bes,8.\fermata\)      | % 2
    r8. \clef "treble^8"
         | % 3
    %bartimesig: 
    \time 2/2 
    \mark  \markup {\italic "Largo"}
    <ees'' f g>1\(      | % 4
    
    
    %%% Parte B
    ees2. r4      | % 5
    f2 r      | % 6
    r1 \clef treble
         | % 7
    ees,      | % 8
    r2. r4      | % 9
    c2 r \clef bass
         | % 10
    \clef bass
    g,4\) r r2 \clef "treble^8"
         | % 11
    %bartimesig: 
    \time 3/16 
    
    
    
    %%% Parte C
    \mark  \markup {\italic "Vivo"}
    <f''' bes>16[ <f bes>] r      | % 12
    r <c, bes'>[\( g'32 f']\)      | % 13
    r8. \clef treble         | % 14
    %bartimesig: 
    \time 2/2 
    
    %%% Parte D
    \mark  \markup {\italic "Largo"}
    c,1\( \sfz      | % 15
    r4 c2. \>      | % 16
    f,2.\) \! \p r4      | % 17
    r1      | % 18
    bes4 r r2      | % 19
    r1      | % 20
    r      | % 21
    r      | % 22
    r \clef "treble^8"
         | % 23
    %bartimesig: 
    \time 3/16 
    
    
    
     %%% Parte E
    \mark  \markup {\italic "Vivo"}
    bes''16[\( g r32 f      | % 24
    f16] r <c a' bes>~      | % 25
    <c a' bes>8 r16      | % 26
    r8 <c, ees f>16~      | % 27
    <c ees f>\) r c'32 a' \clef treble
         | % 28
    r8.      | % 29
    %bartimesig: 
    \time 2/2 
    \mark  \markup {\italic "Largo"}
    r1      | % 30
    r      | % 31
    r      | % 32
    r \bar "|." 
}% end of last bar in partorvoice

 

AvoiceBA = \relative c{
    \set Staff.instrumentName = #""
    \set Staff.shortInstrumentName = #""
    \clef bass
    %staffkeysig
    \key c \major 
    %bartimesig: 
    \time 3/16 
    \partial 16*3
    r8. \f      | % 1
    f,8._\fermata       | % 2
    r8. \clef "bass_8"
         | % 3
    %bartimesig: 
    \time 2/2 
    <ees, f g>1\( \p      | % 4
    ees2. r4      | % 5
    f2 r      | % 6
    r1      | % 7
    r      | % 8
    bes2. r4      | % 9
    r1 \clef bass
         | % 10
    \clef bass
    c4\fp\)  r r2 \clef "bass_8"
         | % 11
    %bartimesig: 
    \time 3/16 
    <f bes>16[ \ff <f bes> <c bes'>~      | % 12
    <c bes'>] r8 \<      | % 13
    r8. \!      | % 14
    %bartimesig: 
    \time 2/2 
    r1 \clef bass
         | % 15
         d4\( \mp r r2      | % 16
    f2. r4      | % 17
    <e d' f>2\) \pp r      | % 18
    r1 \< \mp      | % 19
    f'8 \! r r2.      | % 20
    f16 \f r8. r2.      | % 21
    d,1\fermata  \p      | % 22
    r \clef "bass_8"
         | % 23
    %bartimesig: 
    \time 3/16 
    bes16[\( \ff g r32 f      | % 24
    f16] r8      | % 25
    <f g aes>8.~      | % 26
    <f g aes>16\) r8      | % 27
    r16 <bes ees>32 d' r16 \clef bass
         | % 28
    r8.      | % 29
    %bartimesig: 
    \time 2/2 
    bes'1\( \sfz      | % 30
    <ees,, f d'>2. \> r4      | % 31
    ees'2 \! r      | % 32
    <f bes>1\fermata\)  \pp \bar "|." 
}% end of last bar in partorvoice


\score { 
    << 
        \context PianoStaff <<
        \set PianoStaff.instrumentName="Piano" 
            \context Staff = APnopartA << 
                \context Voice = APnovoiceAA \APnovoiceAA
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
