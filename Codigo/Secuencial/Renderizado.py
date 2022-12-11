import array

HEIGHT = 1024
WIDTH = 960

def create_image():
    data = []
    for i in range(HEIGHT*WIDTH):
        data.append([49, 196, 157])    
    writePPM(data, WIDTH, HEIGHT, "output")

def writePPM(data, width, height, filename):    
    ppm_header = f'P6 {width} {height} {255}\n'
    rgb = []
    for f in data:
        rgb.append(f[0])  # Red
        rgb.append(f[1])  # Green
        rgb.append(f[2])  # Blue
    
    image = array.array('B', rgb)        

    with open(filename + '.ppm', 'wb') as f:        
        f.write(bytearray(ppm_header, 'ascii'))
        image.tofile(f)

def readPPM(path):
    data = []

    with open(path,"rb") as f:
        # read header
        header = f.read(2)
        f.read(1)  # blank
        width = f.read(3)
        f.read(1)  # blank
        height = f.read(3)
        f.read(1)  # blank
        max_val = f.read(3)  # blank
        while (byte := f.read(1)):
            value = int.from_bytes(byte, byteorder='big')
            data.append(value)            
            f.read(1)  # G
            f.read(1)  # B

    return data

def draw_rectangle():
    data = readPPM("output.ppm")
    width = 640
    height = 480
    from_point = width*10
    to_point = width*100
    for i in range(from_point, to_point):        
        data[i] = 255  # negro
    writePPM(data, width, height, "output")

def entrada():
    n = int(input())
    circulos = list()

    for i in range(0,n):
        x = input().split()
        x = map(int,x)    
        circulos.append(list(x))           
    return circulos

if __name__ == "__main__":    
    circulos = entrada()
    print(circulos)
    create_image()

