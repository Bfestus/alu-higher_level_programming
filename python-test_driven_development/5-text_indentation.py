#!/usr/bin/python3
""" Module of indentation
"""


def text_indentation(text):
     """ Text indentation function

    Arguments:
        text (str): A string of text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    str = str.replaceAll("(\\p{Punct})\\s?", "$1\n");
    print(str)
