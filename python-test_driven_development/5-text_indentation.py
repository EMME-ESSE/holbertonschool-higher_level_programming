#!/usr/bin/python3
"""text_indentation module"""


def text_indentation(text):
    """Print the indentation of the given text indented after . ? and : ."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    matches = [".", "?", ":"]
    index = 0
    while index < len(text):
        if text[index] in matches:
            print(f"{text[index]}\n\n", end="")
            index += 1
            while text[index] == " ":
                index += 1
        else:
            print(text[index], end="")
            index += 1