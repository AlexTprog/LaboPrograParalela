import array
from random import randint

# PPM files are human readable files to store images
# first line contains the header having: P3 width height
# second line: the maximum possible color value for each pixel
# Then follows each pixel's data, P3 is plain ASCII and P6 is binary; each pixel contains data for each RGB channel
# See details here: https://en.wikipedia.org/wiki/Netpbm


def writePPM(data, width, height, filename):
    # todo archivo necesita una cabecera, en PPM la cabecera inicia con P6 e indica el anchoe, alto y valor maximo
    ppm_header = f'P6 {width} {height} {255}\n'
    rgb = []
    for f in data:
        rgb.append(f)  # Red
        rgb.append(f)  # Green
        rgb.append(f)  # Blue
    image = array.array('B', rgb)

    with open(filename + '.ppm', 'wb') as f:        
        f.write(bytearray(ppm_header, 'ascii'))
        image.tofile(f)


def readPPM(path):
    data = []

    with open(path) as f:
        # read header
        header = f.read(2)
        f.read(1)  # blank
        width = f.read(3)
        f.read(1)  # blank
        height = f.read(3)
        f.read(1)  # blank
        max_val = f.read(3)  # blank
        while (byte := f.read(1)):
            value = int.from_bytes(byte, byteorder='big')
            data.append(value)
            print(value)
            f.read(1)  # G
            f.read(1)  # B

    return data


def random_image():
    data = []
    height = 480
    width = 640
    max_value = 255
    for i in range(height*width):
        data.append(randint(0, max_value))
    writePPM(data, width, height, "output")


def draw_rectangle():
    data = readPPM("sample.ppm")
    width = 640
    height = 480
    from_point = width*10
    to_point = width*100
    for i in range(from_point, to_point):
        data[i] = 180  # negro
    writePPM(data, width, height, "gray_rectangle")


if __name__ == "_main_":
    random_image()
    # draw_rectangle()
    # draw_square()
    image = "cpu_cache.ppm"