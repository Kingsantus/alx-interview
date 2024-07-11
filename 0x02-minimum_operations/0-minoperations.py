#!/usr/bin/python3
"""
Compute the number of minimum operations needed for copyAll
and paste operations
"""


def minOperations(n: int) -> int:
    """Copmute the minimum Operations needed to get n H characters"""
    up_next = 'H'
    body = 'H'
    op = 0
    while len(body) < n:
        if n % len(body) == 0:
            op += 2
            up_next = body
            body += body
        else:
            op += 1
            body += up_next
    if len(body) != n:
        return 0
    return op
