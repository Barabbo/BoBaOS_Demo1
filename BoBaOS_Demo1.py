import math
import time
import os

# Vertici del cubo
vertices = [
    [-2, -2, -2],
    [2, -2, -2],
    [2, 2, -2],
    [-2, 2, -2],
    [-2, -2, 2],
    [2, -2, 2],
    [2, 2, 2],
    [-2, 2, 2]
]

# Spigoli del cubo
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Facce del cubo
faces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 1, 5, 4),
    (2, 3, 7, 6),
    (1, 2, 6, 5),
    (0, 3, 7, 4)
]

# Luce
light = [0, 0, -1]

# Caratteri per ombreggiare
shading_chars = "-~:;=+"

# Funzione per ruotare i vertici
def rotate_vertices(vertices, angle_x, angle_y, angle_z):
    cosx, sinx = math.cos(angle_x), math.sin(angle_x)
    cosy, siny = math.cos(angle_y), math.sin(angle_y)
    cosz, sinz = math.cos(angle_z), math.sin(angle_z)

    rotated_vertices = []
    for x, y, z in vertices:
        # Rotazione sull'asse X
        y, z = y * cosx - z * sinx, y * sinx + z * cosx
        # Rotazione sull'asse Y
        x, z = x * cosy + z * siny, -x * siny + z * cosy
        # Rotazione sull'asse Z
        x, y = x * cosz - y * sinz, x * sinz + y * cosz
        rotated_vertices.append([x, y, z])
    return rotated_vertices

# Funzione per proiettare i vertici 3D sul piano 2D
def project_vertices(vertices, width, height, scale=10, distance=5):
    projected_vertices = []
    for x, y, z in vertices:
        factor = scale / (z + distance)
        x = x * factor + width / 2
        y = -y * factor + height / 2
        projected_vertices.append((int(x), int(y)))
    return projected_vertices

# Funzione per calcolare la normale di una faccia
def calculate_normal(face, vertices):
    x1, y1, z1 = vertices[face[0]]
    x2, y2, z2 = vertices[face[1]]
    x3, y3, z3 = vertices[face[2]]
    
    ux, uy, uz = x2 - x1, y2 - y1, z2 - z1
    vx, vy, vz = x3 - x1, y3 - y1, z3 - z1
    
    nx = uy * vz - uz * vy
    ny = uz * vx - ux * vz
    nz = ux * vy - uy * vx
    
    length = math.sqrt(nx**2 + ny**2 + nz**2)
    return nx / length, ny / length, nz / length

# Funzione per calcolare l'intensità della luce su una faccia
def calculate_light_intensity(normal, light):
    return max(0, normal[0] * light[0] + normal[1] * light[1] + normal[2] * light[2])

# Funzione per disegnare il cubo nel terminale con ombreggiatura
def draw_cube(vertices, edges, faces, width, height, light):
    screen = [[' ' for _ in range(width)] for _ in range(height)]
    face_intensities = []
    for face in faces:
        normal = calculate_normal(face, vertices)
        intensity = calculate_light_intensity(normal, light)
        face_intensities.append((intensity, face))
    
    face_intensities.sort(reverse=True, key=lambda x: x[0])
    
    for intensity, face in face_intensities:
        shading_char = shading_chars[int(intensity * (len(shading_chars) - 1))]
        pointlist = [vertices[vertex] for vertex in face]
        x1, y1 = project_vertices([pointlist[0]], width, height)[0]
        x2, y2 = project_vertices([pointlist[1]], width, height)[0]
        x3, y3 = project_vertices([pointlist[2]], width, height)[0]
        x4, y4 = project_vertices([pointlist[3]], width, height)[0]
        draw_line(screen, x1, y1, x2, y2, shading_char)
        draw_line(screen, x2, y2, x3, y3, shading_char)
        draw_line(screen, x3, y3, x4, y4, shading_char)
        draw_line(screen, x4, y4, x1, y1, shading_char)
    return screen

# Funzione per disegnare una linea nel terminale
def draw_line(screen, x1, y1, x2, y2, shading_char):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        if 0 <= x1 < len(screen[0]) and 0 <= y1 < len(screen):
            screen[y1][x1] = shading_char
        if x1 == x2 and y1 == y2:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

# Funzione per visualizzare la schermata nel terminale
def display_screen(screen):
    for row in screen:
        print(''.join(row))

# Dimensioni della finestra nel terminale
width, height = 80, 40

# Loop principale
angle_x, angle_y, angle_z = 0, 0, 0
loading_text = "LOADING BOBA OS"
loading_progress = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Ruota i vertici del cubo
    angle_x += 0.03
    angle_y += 0.03
    angle_z += 0.03
    rotated_vertices = rotate_vertices(vertices, angle_x, angle_y, angle_z)
    
    # Proietta i vertici sul piano 2D
    projected_vertices = project_vertices(rotated_vertices, width, height)
    
    # Disegna il cubo nel terminale con ombreggiatura
    screen = draw_cube(rotated_vertices, edges, faces, width, height, light)
    
    # Aggiungi la scritta "LOADING DEMOS"
    if loading_progress < len(loading_text):
        loading_progress += 0.2
    loading_display = loading_text[:int(loading_progress)]
    for i, char in enumerate(loading_display):
        if 0 <= 35 < len(screen) and 0 <= i + (width // 2 - len(loading_text) // 2) < len(screen[0]):
            screen[35][i + (width // 2 - len(loading_text) // 2)] = char

    # Visualizza la schermata nel terminale
    display_screen(screen)

    time.sleep(0.05)
