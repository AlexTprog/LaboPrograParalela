import array
from math import cos, sin

WIDTH = 1024
HEIGHT = 960

FILE = "output.ppm"
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
    width = 0
    height = 0
    with open(path, "rb") as f:
        # read header
        header = f.read(2)
        f.read(1)  # blank
        width = f.read(3)
        f.read(1)  # blank
        height = f.read(3)
        f.read(1)  # blank
        max_val = f.read(3)  # blank
        while (byte := f.read(1)):
            r = int.from_bytes(byte, byteorder='big')
            red.append(r)  # R
            g = int.from_bytes(f.read(1), byteorder='big')
            green.append(g)  # G
            b = int.from_bytes(f.read(1), byteorder='big')
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


def combinarColor(data, new_data):
    color = []
    for i in range(WIDTH*HEIGHT):
        new_color = data[i] ^ new_data[i]
        color.append(int(new_color))
    return color


def entrada():
    n = int(input())
    circulos = list()

    for i in range(0, n):
        x = input().split()
        x = map(int, x)
        circulos.append(list(x))
    return circulos


def draw_cicle(x, y, r, R, G, B):
    red, green, blue = readPPM(FILE)

    for i in range(0, 360):
        xi = int(r*cos(i*PI/180))
        yi = int(r*sin(i*PI/180))
        
        red[(x+xi)*(y+yi)] = red[(x+xi)*(y+yi)] ^ R
        print(red[(x+xi)*(y+yi)])
        green[(x+xi)*(y+yi)] = green[(x+xi)*(y+yi)] ^ G
        blue[(x+xi)*(y+yi)] = blue[(x+xi)*(y+yi)] ^ B
    
    writePPM(red,green,blue,FILE)

if __name__ == "__main__":
    circulos = entrada()
    create_image()
    draw_rectangle()
    # draw_cicle(100, 100, 100, 255, 0, 0)
