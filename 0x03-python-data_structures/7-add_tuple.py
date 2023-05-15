#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    tuple_b = tuple_b[:2] + (0,) * (2 - len(tuple_b))

    result = tuple(sum(x) for x in zip(tuple_a, tuple_b))

    return result
