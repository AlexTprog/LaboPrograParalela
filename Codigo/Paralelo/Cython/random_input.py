import random
WIDTH, HEIGHT = (1024, 960)
FILE = "input.txt"
N = 100

with open(FILE, 'w') as f:
    f.write(str(N))
    for a in range(0, N):
        x = random.randint(-HEIGHT/2, HEIGHT)
        y = random.randint(-WIDTH/2, WIDTH)
        r = random.randint(1, 500)
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        f.write("\n")
        f.write(f"{x} {y} {r} {R} {G} {B}")
