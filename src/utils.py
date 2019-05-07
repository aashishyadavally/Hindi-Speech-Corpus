"""
This script contains utilities which can be used to automate a few processes
in corpus building.

Author:
------
Aashish Yadavally
"""

import itertools


def text_to_unique(path):
    """Generate list of unique words from text transcriptions

    Args:
        path (str):
            Path to file containing text transcriptions
    """
    with open(path, 'r') as text_file:
        contents = text_file.readlines()
    contents = [x.strip().split()[2:] for x in contents]
    words = list(itertools.chain.from_iterable(contents))
    unique_words = sorted(list(set(words)))

    with open('lexicon.txt', 'w') as lex_file:
        for unique_word in unique_words:
            lex_file.write(f'{unique_word}\n')
