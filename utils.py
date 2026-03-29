import settings

def height_perc(percentage):
    return (settings.HEIGHT / 100) * percentage

# print(height_perc(25))

def width_perc(percentage):
    return (settings.WIDTH / 100) * percentage
