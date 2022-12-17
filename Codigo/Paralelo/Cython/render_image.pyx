cimport cython
from cpython cimport array


def imprimir(x: array.array):
    for i in x:
        print(f"FUNCIONA {i}")
    return "x"

cpdef object draw_circle(int x, int y, int r, int R, int G, int B, unsigned char[:] Cr, unsigned char[:]  Cg, unsigned char[:]  Cb, int WIDTH, int HEIGHT):
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

