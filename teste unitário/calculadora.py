# TESTE COM DOCTEST

def soma(x, y):
    """Soma x e y
    >>> soma(10, 20)
    30
    >>> soma(-10, 10)
    0
    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    assertionError: x e y devem ser números
    """
    assert isinstance(x, (int, float)), 'x deve ser número'
    assert isinstance(y, (int, float)), 'y deve ser número'
    return x + y

def subtrai(x, y):
    """Subtrai y de x
    >>> subtrai(10, 5)
    5
    >>> subtrai(-10, -10)
    0
    >>> subtrai('10', 5)
    Traceback (most recent call last):
    ...
    assertionError: x e y devem ser números
    """
    assert isinstance(x, (int, float)), 'x deve ser número'
    assert isinstance(y, (int, float)), 'y deve ser número'
    return x - y

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)