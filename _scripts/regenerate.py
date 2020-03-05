#!/usr/bin/env python
import os
import sys
import string

with open('_scripts/prologue.html', 'r') as f:
    prologue = f.read()

def extract_main_part(f):
    main_part = []
    in_main = False
    for l in f.readlines():
        if l.startswith('<main>'):
            in_main = True
        if in_main:
            main_part.append(l)
    return main_part

def regenerate(p):
    with open(p, 'r') as f:
        main_part = extract_main_part(f)

    with open(p, 'w') as f:
        f.write(prologue + ''.join(main_part))

def main():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                regenerate(os.path.join(root, file))

main()
