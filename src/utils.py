def add_tuples(tuple_a, tuple_b):
    return tuple(a + b for a,b in zip(tuple_a,tuple_b))

def sub_tuples(tuple_a, tuple_b):
    return tuple(a - b for a,b in zip(tuple_a,tuple_b))

def add_to_tuple(num, tuple_a):
    return tuple(a + num for a in tuple_a)

def sub_to_tuple(num, tuple_a):
    return tuple(a - num for a in tuple_a)