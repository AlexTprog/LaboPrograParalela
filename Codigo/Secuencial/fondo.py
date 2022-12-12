import array 
import image_processing
from random import randint

width=1600
height=1200

# PPM files are human readable files to store images
# first line contains the header having: P3 width height
# second line: the maximum possible color value for each pixel
# Then follows each pixel's data, P3 is plain ASCII and P6 is binary; each pixel contains data for each RGB channel
# See details here: https://en.wikipedia.org/wiki/Netpbm
def writePPM(red, green, blue, filename):
  # todo archivo necesita una cabecera, en PPM la cabecera inicia con P6 e indica el anchoe, alto y valor maximo
  ppm_header = f'P6 {width} {height} {255}\n'
  rgb = []
  for i in range(len(red)):
      rgb.append(red[i]) # Red 
      rgb.append(blue[i]) # Blue
      rgb.append(green[i]) # Green 
  image = array.array('B', rgb)

  with open(filename, 'wb') as f:
    f.write(bytearray(ppm_header, 'ascii'))
    image.tofile(f)


def readPPM(path):
    red = []
    green = []
    blue = []
    width = 0
    height = 0
    with open(path, "rb") as f:
        # read header
        header = f.read(2)
        f.read(1) # blank
        width = f.read(3)
        f.read(1) # blank
        height = f.read(3)
        f.read(1) # blank
        max_val = f.read(3) # blank
        while (byte := f.read(1)):
            r = int.from_bytes(byte, byteorder='big')
            red.append(r) # R
            g = int.from_bytes(f.read(1), byteorder='big')
            green.append(g) # G
            b = int.from_bytes(f.read(1), byteorder='big')
            blue.append(b) # B

    return red, green, blue

#def random_image():
#    data = []
#    max_value = 255
#    for i in range(height*width):
#        data.append(randint(0, max_value))
#    writePPM(data, width, height, "output")

#def draw_rectangle():
#    data = readPPM("sample.ppm")
#    width = 640
#    from_point = width*10
#    to_point = width*100
#    for i in range(from_point, to_point):
#        data[i] = 180 # negro
#    writePPM(data, width, height, "gray_rectangle")

#def draw_square():
#    data = readPPM("cpu_photo_640_480.ppm")
#    from_line = 189
#    to_line = 423
#    from_column = 467
#    to_column = 526
#    for i in range(from_line, to_line):
#        for j in range(from_column, to_column):
#            index = j+i*width
#            data[index] = 0 # negro
#    writePPM(data, width, height, "black_square_cpu_photo")

def gaussian_blur(image, output_filename):
    red, blue, green = readPPM(image)

    new_red = average(array.array("i", red), width, height)
    new_green = average(array.array("i", green), width, height)
    new_blue = average(array.array("i", blue), width, height)
    writePPM(new_red, new_green, new_blue, output_filename)

## vamos a pasar esta funcion a Cython
#def compute_internal_pixel(data, i):
#    #                       derecha     izquierda     arriba          abajo
#    val = data[i] + data[i+1] + data[i-1] + data[i-width] + data[i+width] 
#    #            abajo-derecha     arriba-derecha    abajo-izquierda   arriba-izquierda
#    val += data[i+1+width] + data[i+1-width] + data[i-1+width] + data[i-1-width] 
#    return val/9

def average(data, width, height):
    filtered = []
    # multiprocessing o puedo hacer OpenMP en cython
    for i in range(height*width):
        new_pixel = image_processing.compute_pixel(data, i, width, height)
        filtered.append(int(new_pixel))
    return filtered


if __name__ == "__main__":
    #random_image()
    #draw_rectangle()
    #draw_square()
    image = "flowers-1.ppm"
    output = "flower_blurred.ppm"
    gaussian_blur(image, output)