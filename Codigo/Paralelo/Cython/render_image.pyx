from cython cimport cdivision, cdivision_warnings, boundscheck
from cpython cimport array
from cython.parallel import prange
cimport cython


@boundscheck(False)
@cdivision(True)
def draw_circle(int x, int y, int r, int R, int G, int B, array.array Cr, array.array Cg, array.array Cb, int WIDTH, int HEIGHT):
    cdef int i
    cdef int xi
    cdef int yi
    cdef int rg = (2*r+1)**2
    cdef int rg2 = 2*r+1
    cdef int w = WIDTH
    cdef int h = HEIGHT

    # Iterar sobre las coordenadas x e y desde -r hasta r
    for i in prange(rg, nogil=True):
        xi = i % rg2 - r
        yi = i // rg2 - r
        # Verificar si el punto actual está fuera de los límites de la imagen
        if x + xi < 0 or x + xi >= w or y + yi < 0 or y + yi >= h:
            continue

        # Verificar si el punto actual está dentro del círculo
        if xi*xi + yi*yi <= r*r:
            # Modificar los valores RGB en el pixel correspondiente en la imagen
            Cr.data.as_ints[(y+yi)*w + (x+xi)
                            ] = Cr.data.as_ints[(y+yi)*w + (x+xi)] ^ R
            Cg.data.as_ints[(y+yi)*w + (x+xi)
                            ] = Cg.data.as_ints[(y+yi)*w + (x+xi)] ^ G
            Cb.data.as_ints[(y+yi)*w + (x+xi)
                            ] = Cb.data.as_ints[(y+yi)*w + (x+xi)] ^ B

    # Escribir el contenido de la imagen modificada al archivo PPM
    return Cr, Cg, Cb
