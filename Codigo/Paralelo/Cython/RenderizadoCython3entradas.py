import array
import render_image

WIDTH, HEIGHT = (1024, 960)
FILE = "salida.ppm"
PI = 3.14159


def create_image():
    r = [0]*(HEIGHT * WIDTH)
    g = [0]*(HEIGHT * WIDTH)
    b = [0]*(HEIGHT * WIDTH)
    return r, g, b


def writePPM(R, G, B, filename):
    ppm_header = f'P6 {WIDTH} {HEIGHT} {255}\n'
    rgb = []
    for i in range(len(R)):
        r = R[i]
        g = G[i]
        b = B[i]
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
        circulos.append(tuple(x))
    return circulos


if __name__ == "__main__":
    circulos = entrada()
    r, g, b = create_image()
    render_image.imprimir(array("i", [1, 2, 3, 4, 5, 6]))
    
    # for c in circulos:
    #     r, g, b = rd.draw_circle(
    #         c[0], c[1], c[2], c[3], c[4], c[5], bytes(r), bytes(g), bytes(b), WIDTH, HEIGHT)
    #     #r, g, b = rd.draw_circle(
    #     #   c[0], c[1], c[2], c[3], c[4], c[5], r, g, b, WIDTH, HEIGHT)
    # writePPM(r, g, b, FILE)

def draw_cicle(x, y, r, R, G, B, Cr, Cg, Cb):
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
