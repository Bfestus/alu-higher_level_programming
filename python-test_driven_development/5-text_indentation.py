#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuations:
            lines.append(current_line.strip())
            current_line = ""

    if current_line.strip():
        lines.append(current_line.strip())

    for line in lines:
        print(line + "\n\n", end='')

