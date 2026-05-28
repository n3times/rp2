# Choose values that produce the same output as the first
# known rendering of the Mandelbrot set.

MAX_ITERS = 200
ROWS, COLS = 31, 71
MIN_X, MAX_X = -1.975, 0.475
MIN_Y, MAX_Y = -0.8715, 0.8715

def is_in_mandelbrot(c):
    z = 0
    for _ in range(MAX_ITERS):
        if abs(z) > 2: return False
        z = z * z + c
    return True

def translate(col, row):
    real = MIN_X + col / (COLS - 1) * (MAX_X - MIN_X)
    imag = MIN_Y + row / (ROWS - 1) * (MAX_Y - MIN_Y)
    return complex(real, imag)

for row in range(ROWS):
    for col in range(COLS):
        c = translate(col, row)
        print("*" if is_in_mandelbrot(c) else " ", end="")
    print()
