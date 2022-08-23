#!/usr/bin/python3
"""Documentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after
    each of these characters: ., ? and :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for c in text:
        line += c
        if c in ['.', '?', ':']:
            print((line + '\n').lstrip(' '))
            line = ""
    print(line.lstrip(' '), end="")
