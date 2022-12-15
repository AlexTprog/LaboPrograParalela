import array
import struct
import math
from math import cos, sin
from multiprocessing import Pool
WIDTH, HEIGHT = (1024, 960)
pool = Pool(processes=8)
FILE = "salidaTest.ppm"
PI = 3.14159


def create_image():

    pixels = [(0, 0, 0)] * (HEIGHT * WIDTH)

    # Convertir la lista de tuplas de pixeles en tres arreglos
    # separados para los valores de rojo, verde y azul

    # Escribir la imagen en el archivo PPM
    writePPM(pixels, FILE)


def writePPM(pixels, filename):
    ppm_header = f'P6 {WIDTH} {HEIGHT} {255}\n'
    rgb = []
    for i in range(len(pixels)):
        r, g, b = pixels[i]
        rgb.append(r)  # Red
        rgb.append(g)  # Green
        rgb.append(b)  # Blue
    image = array.array('B', rgb)
    with open(filename, 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        image.tofile(f)


def readPPM(path):
    # Crear una matriz para almacenar los valores RGB de todos los pixeles
    pixels = []

    with open(path, "rb") as f:
        # read header
        header = f.read(2)

        # Convertir la variable header a un objeto de tipo str
        # si es necesario
        if isinstance(header, bytes):
            header = header.decode()

        if header.strip() != "P6":
            raise ValueError("Invalid PPM header")
        # read width, height, and max color value
        width, height, max_val = [int(x)
                                  for x in f.readline().decode().split()]

        # read pixel values
        for i in range(width*height):
            # Leer los valores de los pixeles utilizando la función
            # struct.unpack en lugar de int.from_bytes
            r, g, b = struct.unpack('>BBB', f.read(3))
            pixels.append((r, g, b))

    # Desempaquetar las tuplas de pixeles en tres arreglos separados
    # para los valores de rojo, verde y azul

    return pixels


def draw_rectangle():
    red, green, blue = readPPM(FILE)
    for i in range(WIDTH*10, WIDTH*100):
        # Modificar los valores RGB en el pixel correspondiente en la imagen
        red[i] = 0
        green[i] = 255
        blue[i] = 0
    writePPM(red, green, blue, FILE)


def entrada():
    n = int(input())
    circulos = []

    for i in range(0, n):
        x = input().split()
        x = map(int, x)
        circulos.append(tuple(x))  # <-- Crear una tupla
    return circulos


def draw_cicle(x, y, r, R, G, B):
    # Leer el contenido del archivo PPM
    pixels = readPPM(FILE)

    # Iterar sobre las coordenadas x e y desde -r hasta r
    for xi in range(-r, r+1):
        for yi in range(-r, r+1):
            # Verificar si el punto actual está fuera de los límites de la imagen
            if x + xi < 0 or x + xi >= WIDTH or y + yi < 0 or y + yi >= HEIGHT:
                continue

            # Verificar si el punto actual está dentro del círculo
            if xi*xi + yi*yi <= r*r:
                # Modificar los valores RGB en el pixel correspondiente en la imagen
                pixels[(y+yi)*WIDTH + (x+xi)] = (R, G, B)

    # Escribir el contenido de la imagen modificada al archivo PPM
    writePPM(pixels, FILE)


if __name__ == "__main__":
    circulos = entrada()
    create_image()
    with Pool() as pool:

        for c in circulos:
            pool.starmap(draw_cicle, [c])
