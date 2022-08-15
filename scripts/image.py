from colour import Color
from PIL import Image as im
from tqdm import tqdm
import numpy as np

from my_library.my_module.my_functions import mandelbrot_image

center = complex(0.4200101, 0.20101023)
zoom = 30.0
resolution = (64, 64)
levels = 80

red = Color("red")
blue = Color("blue")
cmap = list(red.range_to(blue, levels + 1))

array = mandelbrot_image(center, 1.0 / zoom, resolution, levels)
shape = array.shape

image = np.zeros((shape[1], shape[0], 3), dtype=np.uint8)

for n in tqdm(range(resolution[0] * resolution[1])):
    j = n % resolution[1]
    i = n // resolution[1]
    [r, g, b] = cmap[int(array[i, j])].rgb
    image[j, i, 0] = r * 255.0
    image[j, i, 1] = g * 255.0
    image[j, i, 2] = b * 255.0

data = im.fromarray(image)
data.save("result.png")
