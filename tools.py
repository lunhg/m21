import os
import re

def lytexify(lilypondpath):
    """Create a .lytex, and compile a .tex file for use scores in LaTeX"""
    # lytex file is a simple one line file
    os.system("echo \\\lilypondfile\{%s.ly\} > %s.lytex" % (lilypondpath, lilypondpath))

    # compile lytex for specific output
    s = lilypondpath.split("/")
    s = s[:len(s)-1]
    s = "/".join(s)
    os.system("lilypond-book %s.lytex -o %s" % (lilypondpath, s))
    
    # replace new path on compiled file
    f = open("%s.tex" % lilypondpath, 'r')
    filedata = f.read()
    newdata  =filedata.replace("\input{", "\input{.%s/" % s)

    # catch generated files
    gen = re.findall('[A-Za-z0-9]{2}/lily-[A-Za-z0-9]*', filedata)[0]
    print gen

    # write new path
    f = open("%s.tex" % lilypondpath, 'w')
    f.write(newdata)
    f.close()

    # now we need to change auxiliary files (the generated ones in generated dir)
    f = open("%s/%s-systems.tex" % (s, gen), 'r')
    filedata = f.read()
    f.close()
    newdata = filedata.replace("includegraphics{", "includegraphics{.%s/" % s)

    # write new path
    f = open("%s/%s-systems.tex" % (s, gen), 'w')
    f.write(newdata)
    f.close()

