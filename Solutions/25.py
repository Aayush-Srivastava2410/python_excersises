def my_func(n1:int, n2:int, add:bool=True ):
    '''Adds/ Subtracts 2 numbers.
    ----------------------------------------------------------------
    Attributes

    n1:`int`
        Number 1
    n2:`int`
        Number 2
    add:bool
        Add 2 numbers or subtracts 2 numbers. Defaults to add
    '''
    if add:
        return n1 + n2
    else:
        return n1 - n2
    

