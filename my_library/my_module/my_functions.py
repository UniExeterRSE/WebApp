def mandelbrot(c: complex, max_iter: int = 80) -> int:
    """
    Calculate the number of iterations required to reach a modulus greater than 2.
    If the number of iterations is greater than max_iter, stop and return max_iter.

    Args:
        c (complex): Complex number to evaluate.
        c (int): Maximum number of iterations to perform.

    Returns:
        int: Number of iterations required to reach a modulus greater than 2.
    """
    z = 0
    n = 0
    while abs(z) <= 2.0 and n < max_iter:
        z = z * z + c
        n += 1
    return n
