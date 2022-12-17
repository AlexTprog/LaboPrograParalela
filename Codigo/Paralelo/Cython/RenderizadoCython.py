import array as a
import render_image as rd

WIDTH, HEIGHT = (1024, 960)
FILE = "salida.ppm"
PI = 3.14159


def create_image():
    rgb = a.array('i', [0] * (WIDTH * HEIGHT) * 3)
    r, g, b = rgb[::3], rgb[1::3], rgb[2::3]
    return r, g, b



def writePPM(R, G, B, filename):
    ppm_header = f'P6 {WIDTH} {HEIGHT} {255}\n'
    rgb = []
    for i in range(len(R)):        
        rgb.append(R[i])  # Red
        rgb.append(G[i])  # Green
        rgb.append(B[i])  # Blue
    image = a.array('B', rgb)
    with open(filename, 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        image.tofile(f)


def draw_circle(x, y, r, R, G, B, Cr, Cg, Cb):
    # Iterar sobre las coordenadas x e y desde -r hasta r
    for xi in range(-r, r+1):
        for yi in range(-r, r+1):
            # Verificar si el punto actual está fuera de los límites de la imagen
            if x + xi < 0 or x + xi >= WIDTH or y + yi < 0 or y + yi >= HEIGHT:
                continue

            # Verificar si el punto actual está dentro del círculo
            if xi*xi + yi*yi <= r*r:
                # Modificar los valores RGB en el pixel correspondiente en la imagen
                Cr[(y+yi)*WIDTH + (x+xi)] = Cr[(y+yi)*WIDTH + (x+xi)] ^ R
                Cg[(y+yi)*WIDTH + (x+xi)] = Cg[(y+yi)*WIDTH + (x+xi)] ^ G
                Cb[(y+yi)*WIDTH + (x+xi)] = Cb[(y+yi)*WIDTH + (x+xi)] ^ B
    
    return Cr, Cg, Cb


def entrada():
    n = int(input())
    circulos = []

    for i in range(0, n):
        x = input().split()
        x = map(int, x)
        circulos.append(tuple(x))
    return circulos


if __name__ == "__main__":
    circulos = entrada()
    r, g, b = create_image()
    for c in circulos:
        r, g, b = rd.draw_circle(
            c[0], c[1], c[2], c[3], c[4], c[5], r, g, b, WIDTH, HEIGHT)
    writePPM(r, g, b, FILE)
