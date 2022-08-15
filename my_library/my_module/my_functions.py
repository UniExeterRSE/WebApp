from typing import Union
import numpy as np
from tqdm import tqdm


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


def mandelbrot_image(
    center: complex,
    scale: float,
    resolution: Union[int, int] = (512, 512),
    max_iter: int = 80,
) -> np.ndarray:
    """
    Sample a region of the Mandelbrot set.
    """

    aspect_ratio = float(resolution[1]) / float(resolution[0])
    mins = complex(center.real - scale, center.imag - (scale * aspect_ratio))
    maxs = complex(center.real + scale, center.imag + (scale * aspect_ratio))

    delta = complex(
        (maxs.real - mins.real) / (resolution[0] - 1),
        (maxs.imag - mins.imag) / (resolution[1] - 1),
    )

    result = np.zeros(resolution, dtype=np.uint8)
    for n in tqdm(range(resolution[0] * resolution[1])):
        j = n % resolution[1]
        i = n // resolution[1]
        im = mins.imag + (delta.imag * j)
        re = mins.real + (delta.real * i)
        result[i, j] = mandelbrot(complex(re, im), max_iter)
    return result
