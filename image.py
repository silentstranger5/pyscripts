import numpy as np
from PIL import Image, ImageFilter, ImageChops
from scipy import ndimage


def apply_filters(filename, path):
    ext = filename.split('.')[-1]
    filepath = path + '/' + filename
    get_path = lambda name: path + '/' + name + '.' + ext
    image_process(filepath, get_path("brighten"), brightness, 2)
    image_process(filepath, get_path("darken"), brightness, 0.25)
    image_process(filepath, get_path("high_contrast"), contrast, 2)
    image_process(filepath, get_path("low_contrast"), contrast, 0.25)
    image_process(filepath, get_path("grayscaled"), grayscale)
    image_process(filepath, get_path("blurred"), blur, 16)
    image_process(filepath, get_path("sobel"), sobel)


def image_process(infile, outfile, function, *args):
    image = Image.open(infile)
    result = function(image, *args)
    result.save(outfile)


def brightness(image, factor):
    return image.point(lambda i: i * factor)


def contrast(image, factor):
    return image.point(lambda i: (i - (256 // 2)) * factor + (256 // 2))


def grayscale(image):
    r, g, b = image.split()
    vector = (0.299, 0.587, 0.114)
    r, g, b = (r.point(lambda i: i * factor) for factor in vector)
    return sum_chanels(r, g, b)


def sum_chanels(r, g, b):
    return ImageChops.add(ImageChops.add(r, g), b)


def blur(image, kernel):
    return image.filter(ImageFilter.BoxBlur(kernel // 2))


def sobel(image):
    converted = image.convert("L")
    array = np.asarray(converted)
    array = array.astype('float')
    matrix_x = ((1, 0, -1), (2, 0, -2), (1, 0, -1))
    matrix_y = ((1, 2, 1), (0, 0, 0), (-1, -2, -1))
    sobel_x = ndimage.convolve(array, matrix_x)
    sobel_y = ndimage.convolve(array, matrix_y)
    magnitude = np.hypot(sobel_x, sobel_y)
    magnitude *= 255.0 / np.max(magnitude)
    magnitude = np.uint8(magnitude)
    return Image.fromarray(magnitude)


apply_filters("image.jpg", "image")
