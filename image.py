import sys
from PIL import Image, ImageFilter, ImageChops


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
    return image.filter(ImageFilter.FIND_EDGES)


if __name__ == '__main__':
    if not sys.argv or len(sys.argv) < 4:
        print("Usage: python image.py <input> <output> <filter> <value>\n"
              "Filters: brightness contrast grayscale blur sobel")
        exit(1)

    infile = sys.argv[1]
    outfile = sys.argv[2]
    filter = sys.argv[3]
    value = sys.argv[4] if len(sys.argv) > 4 else None

    filter = filter.strip().lower()
    value = float(value) if value else None

    match filter:
        case "brightness":
            image_process(infile, outfile, brightness, value)

        case "contrast":
            image_process(infile, outfile, contrast, value)

        case "grayscale":
            image_process(infile, outfile, grayscale)

        case "blur":
            image_process(infile, outfile, blur, value)

        case "sobel":
            image_process(infile, outfile, sobel)
