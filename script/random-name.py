#!/usr/bin/env python2.7
"""
This script is used to generate a random name.  It's useful for unique project
names.

The search algorithm loads the text files line-by-line, so as not to use up so
much RAM.  It's a little slower than caching all of the files, but more memory
efficient.
"""
# Imports ######################################################################
from __future__ import print_function
import os
from functools import partial
from random import randint

# Metadata #####################################################################
__author__ = "Timothy McFadden"
__date__ = "09/16/2014"
__copyright__ = "Avago Technologies, 2014"
__license__ = "Proprietary"
__version__ = "0.01"

# Globals ######################################################################
USER_CHARS = {}
THIS_DIR = os.path.abspath(os.path.dirname(__file__))

NOUN_FILE = os.path.join(THIS_DIR, 'data', 'noun.txt')
MAX_NOUN = 55236

ADVERB_FILE = os.path.join(THIS_DIR, 'data', 'adverb.txt')
MAX_ADVERB = 3641

ADJECTIVE_FILE = os.path.join(THIS_DIR, 'data', 'adjective.txt')
MAX_ADJECTIVE = 17889

VERB_FILE = os.path.join(THIS_DIR, 'data', 'verb.txt')
MAX_VERB = 8430


def _get_random_word(word_file, max_index):
    """Open a file and retrieve the line at index `index`."""
    index = randint(0, max_index)

    with open(word_file, 'rb') as fh:
        for line_num, line in enumerate(fh):
            if line_num == index:
                return line.strip()

        # Return the last line just in case `index` > MAX
        return line


FUNC_MAP = {
    "N": partial(_get_random_word, NOUN_FILE, MAX_NOUN),
    "V": partial(_get_random_word, VERB_FILE, MAX_VERB),
    "J": partial(_get_random_word, ADJECTIVE_FILE, MAX_ADJECTIVE),
    "A": partial(_get_random_word, ADVERB_FILE, MAX_ADVERB),
}


def random_name(template, join_char="-"):
    """Return a random name based on the template."""
    result = []
    for char in template:
        if char in FUNC_MAP:
            result.append(FUNC_MAP[char]())
        elif char in USER_CHARS:
            result.append(USER_CHARS[char])
        else:
            raise ValueError("Unknown template character [%s]" % char)

    return join_char.join(result)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="""\
This script generates a random name based on the template provide, and using the
data from Princeton's WordNet project.

The template used is: J -- an adjective, N -- a noun, V -- a verb, A -- an adverb.

Example:
    "JNN" -- A single adjective followed by two nouns""")
    parser.add_argument('--template', help="Template used for name.  E.g. 'JN' (adjective-noun)", type=str, default="JN")
    parser.add_argument('--count', help="Number of names to generate", type=int, default=5)
    parser.add_argument('--join', help="Character used to join the name parts", type=str, default="-")
    parser.add_argument('--chars', help="Constant-word template char.  E.g. 'X,word1 Y,word2'", nargs="+", default=[])
    args = parser.parse_args()

    USER_CHARS = {key: value for key, value in [x.split(",") for x in args.chars]}

    for _ in xrange(args.count):
        print(random_name(args.template, args.join))
