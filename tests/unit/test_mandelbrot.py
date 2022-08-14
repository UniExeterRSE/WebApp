def test_mandelbrot():
    from my_library.my_module.my_functions import mandelbrot

    assert mandelbrot(complex(2.0, 2.0)) == 1
    assert mandelbrot(complex(1.1, 0.1)) == 2
    assert mandelbrot(complex(0.1, 1.1)) == 4
    assert mandelbrot(complex(0.5, 0.5)) == 5
    assert mandelbrot(complex(0.1, 0.1)) == 80
