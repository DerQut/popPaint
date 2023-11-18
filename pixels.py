import paint

def generate_pixels(surface, colour, x_size, y_size, p_x_size, p_y_size):

    x = 0
    y = 0

    table = []

    while y < y_size:
        while x < x_size:
            table.append(paint.Pixel(surface, colour, x, y, p_x_size, p_y_size))
            x = x + p_x_size
        y = y + p_y_size
        x = 0
