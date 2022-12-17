import array

WIDTH, HEIGHT = (1024, 960)
FILE = "salida.ppm"
PI = 3.14159


def create_image():

    pixels = [(0, 0, 0)] * (HEIGHT * WIDTH)

    # Convertir la lista de tuplas de pixeles en tres arreglos
    # separados para los valores de rojo, verde y azul

    return pixels


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


def entrada():
    n = int(input())
    circulos = []

    for i in range(0, n):
        x = input().split()
        x = map(int, x)
        circulos.append(tuple(x))  # <-- Crear una tupla
    return circulos


def draw_circle(c, pixels):
    x, y, r, R, G, B = c[0], c[1], c[2], c[3], c[4], c[5]

    # Iterar sobre las coordenadas x e y desde -r hasta r
    for xi in range(-r, r+1):
        for yi in range(-r, r+1):
            # Verificar si el punto actual está fuera de los límites de la imagen
            if x + xi < 0 or x + xi >= WIDTH or y + yi < 0 or y + yi >= HEIGHT:
                continue

            # Verificar si el punto actual está dentro del círculo
            if xi*xi + yi*yi <= r*r:
                # Modificar los valores RGB en el pixel correspondiente en la imagen
                pixels[(y+yi)*WIDTH + (x+xi)] = (
                    pixels[(y+yi)*WIDTH + (x+xi)][0] ^ R,
                    pixels[(y+yi)*WIDTH+(x+xi)][1] ^ G,
                    pixels[(y+yi)*WIDTH + (x+xi)][2] ^ B)

    return pixels


if __name__ == "__main__":
    circulos = entrada()
    pixels = create_image()
    for c in circulos:
        pixels = draw_circle(c, pixels)

    writePPM(pixels, FILE)
