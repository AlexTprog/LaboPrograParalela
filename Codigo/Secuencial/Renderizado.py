def entrada():
    n = int(input())
    circulos = list()

    for i in range(0,n):
        x = input().split()
        x = map(int,x)    
        circulos.append(list(x))   
    
    print(circulos)             
    return circulos

if __name__ == "__main__":    
    entrada()

# Crea fondo
# Dibujar circulos - Colorear
## Resolver intersecciones