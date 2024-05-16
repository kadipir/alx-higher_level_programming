#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    if sentence:
        length = len(sentence)
        first = sentence[:1]
    else:
        length = 0
    return (length, first)

