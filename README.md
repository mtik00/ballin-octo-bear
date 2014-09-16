Introduction
============

This is a quick and dirty script to generate a random project name, a bit like
GitHub's name generator.

It uses the data files from [Princeton's WordNet project](http://wordnet.princeton.edu/wordnet/download/current-version/).

Usage
=====

There's only one script in this package: `random-name.py`.  Use this script to
generate a random name from the specified template (the default is "JN", meaning
"adjective-noun").

    > python random-name.py
    attitudinal-ceremony
    surreal-microbe
    epicurean-rum
    arching-shift
    naiant-fibrinopeptide

Run the script with `--h` to see the other options.  Here's a more complex
example that loosely resembles GitHub's name generator:

    > python random-name.py --template "JXN" --chars X,octo --count 1
    acceptable-octo-battalion

You must also include the "data" directory when distibuting/running the script.

Other than that, the script only uses Python built-ins, and requires no addition
packages.  This script has been test on Windows Python 2.7, although I see no
reason the script would not run on other operating systems.

Template
========

The _template_ is a string of single-character identifiers.  The following
identifiers are built in:
* N -- A noun
* V -- A verb
* J -- An adverb
* A -- An adjective

Using this table, `--template "JN"` would produce a two-word name with an adverb
for the first word and a noun for the second.  Example: `hooflike-piffle`.

You also have the option of using `--chars` to add your own _constant word_
identifiers.  You can use any single character, but it's best to **not** overwrite
the defaults.  This command-line parameter should be a list of comma-separated
"key,word" pairs.  For example: `--chars X,me Y,you Z,them`.  Using
`--chars X,me Y,you Z,them --template "XAYNZ"` would` could produce
`me-bolt-you-sapote-them`.

Word Data
=========

The words are pretty much unadulterated from the original WordNet list.  This
list only includes words solely comprized of the letters `a` through `z`.  You
may wish to ensure the recommended name is appropriate for your workplace!
