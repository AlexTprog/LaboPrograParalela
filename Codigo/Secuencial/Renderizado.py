import array
from math import cos, sin
from multiprocessing import Pool
WIDTH = 1024
HEIGHT = 960

FILE = "salida.ppm"
PI = 3.14159


def create_image():
    red = []
    green = []
    blue = []
    for i in range(HEIGHT*WIDTH):
        red.append(0)
        green.append(0)
        blue.append(0)
    writePPM(red, green, blue, FILE)


def writePPM(red, green, blue, filename):
    ppm_header = f'P6 {WIDTH} {HEIGHT} {255}\n'
    rgb = []
    for i in range(len(red)):
        rgb.append(red[i])  # Red
        rgb.append(green[i])  # Green
        rgb.append(blue[i])  # Blue
    image = array.array('B', rgb)
    with open(filename, 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        image.tofile(f)


def readPPM(path):
    red = []
    green = []
    blue = []

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
            r = int.from_bytes(f.read(1), byteorder='big')
            g = int.from_bytes(f.read(1), byteorder='big')
            b = int.from_bytes(f.read(1), byteorder='big')
            red.append(r)
            green.append(g)

            blue.append(b)  # B

    return red, green, blue


def draw_rectangle():
    red, green, blue = readPPM(FILE)
    from_point = WIDTH*10
    to_point = WIDTH*100

    for i in range(from_point, to_point):
        red[i] = red[i] ^ 0
        green[i] = green[i] ^ 255
        blue[i] = blue[i] ^ 0
    writePPM(red, green, blue, FILE)


def entrada():
    n = int(input())
    circulos = list()

    for i in range(0, n):
        x = input().split()
        x = map(int, x)
        circulos.append(list(x))
    return circulos


def draw_cicle(x, y, r, R, G, B):
    # Leer el contenido del archivo PPM
    red, green, blue = readPPM(FILE)

    # Iterar sobre las coordenadas x e y desde -r hasta r
    for xi in range(-r, r+1):
        for yi in range(-r, r+1):
            # Verificar si el punto actual está fuera de los límites de la imagen
            if x + xi < 0 or x + xi >= WIDTH or y + yi < 0 or y + yi >= HEIGHT:
                continue

            # Verificar si el punto actual está dentro del círculo
            if xi*xi + yi*yi <= r*r:
                # Modificar los valores RGB en el pixel correspondiente en la imagen
                red[(y+yi)*WIDTH+(x+xi)] = R
                green[(y+yi)*WIDTH+(x+xi)] = G
                blue[(y+yi)*WIDTH+(x+xi)] = B

    # Escribir el contenido de la imagen modificada al archivo PPM
    writePPM(red, green, blue, FILE)


if __name__ == "__main__":
    circulos = entrada()
    create_image()
    with Pool(processes=4) as pool:
        pool.starmap(draw_cicle, circulos)
