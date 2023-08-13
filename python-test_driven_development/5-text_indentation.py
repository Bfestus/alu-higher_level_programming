#!/usr/bin/python3
"""
    Module containing text indentation function
"""


def text_indentation(text):
    """ Text indentation function

    Arguments:
        text (str): A string of text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    list_punctuation = [".", "?", ":"]
    lines = []
    current_line = ""
    for char in text:
        current_line += char
        if char in list_punctuation:
            lines.append(current_line.strip())
            current_line = ""
    
    if current_line.strip():
        lines.append(current_line.strip())
    
    for line in lines:
        print(line + "\n\n", end='')        
