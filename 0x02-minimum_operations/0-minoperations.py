#!/usr/bin/env python3
'''Minimum Operations Challenge'''


def minOperations(n):
    '''calculates the fewest number of operations needed to result in exactly n H characters in this file.
        Returns:
          Integer: if n is impossible to achieve, return 0
    '''
    pasted_chars = 1  # current number of chars in the file
    clipboard = 0  # how many H's copied
    counter = 0  # operations counter

    while pasted_chars < n:
        # if did not copy anything yet
        if clipboard == 0:
            clipboard = pasted_chars
            counter += 1

        # if haven't pasted anything yet
        if pasted_chars == 1:
            pasted_chars += clipboard
            counter += 1
            continue
        
        # remaining chars to Paste
        remaining = n - pasted_chars
        if remaining < clipboard:
            return 0

        # if can't be devided
        if remaining % pasted_chars != 0:
            pasted_chars += clipboard
            counter += 1
        else:
            clipboard = pasted_chars
            pasted_chars += clipboard
            counter += 2

    # if got the desired result
    if pasted_chars == n:
        return counter
    else:
        return 0
