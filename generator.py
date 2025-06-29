import turtle
from PIL import Image


def generate_pattern(sides=5, depth=10, size=100, angle=20, color='blue', pattern_type='polygon', output_path='static/images/pattern.png'):
    """
    Génère un motif géométrique selon le type demandé et sauvegarde le résultat en PNG.

    :param sides: Nombre de côtés du polygone (minimum 3)
    :param depth: Nombre de répétitions ou profondeur
    :param size: Taille initiale du motif
    :param angle: Angle de rotation entre chaque répétition
    :param color: Couleur du motif
    :param pattern_type: Type de motif : 'polygon', 'spiral', 'fractal'
    :param output_path: Chemin de sauvegarde de l'image
    """

    # Sécurité sur la taille pour éviter les bugs
    max_size = 400
    if size > max_size:
        print(f"[Info] Taille trop grande ({size}), limitation à {max_size}")
        size = max_size

    if sides < 3:
        sides = 3

    # Configuration de la fenêtre Turtle
    screen = turtle.Screen()
    screen.setup(width=1000, height=1000)
    screen.bgcolor('white')

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color(color)

    t.penup()
    t.goto(-size // 2, -size // 2)
    t.pendown()

    # Choix du motif
    if pattern_type == 'polygon':
        t.penup()
        t.goto(0, 0)
        t.pendown()
        for _ in range(depth):
            for _ in range(sides):
                t.forward(size)
                t.right(360 / sides)
            t.right(angle)

    elif pattern_type == 'spiral':
        t.penup()
        t.goto(0, 0)
        t.pendown()

        total_steps = depth * sides
        distance = size / total_steps  # Distance de départ plus proportionnelle

        for i in range(total_steps):
            t.forward(distance * i)
            t.right(angle)


    elif pattern_type == 'fractal':
    # Centrage du motif fractal
        t.penup()
        t.goto(0, 0)
        t.pendown()

    # Appel de la fonction fractale avec profondeur fixée
        fractal_star(t, size, sides, depth=3)


    else:
        print(f"[Avertissement] Type inconnu '{pattern_type}', utilisation du polygone par défaut")
        for _ in range(depth):
            for _ in range(sides):
                t.forward(size)
                t.right(360 / sides)
            t.right(angle)

    # Sauvegarde en PNG via EPS
    canvas = screen.getcanvas()
    canvas.postscript(file="temp.eps")

    img = Image.open("temp.eps")
    img.save(output_path, 'png')

    turtle.clearscreen()
    screen.bye()

    print(f"[OK] Motif '{pattern_type}' généré et sauvegardé : {output_path}")


def fractal_star(t, length, sides, depth=3):
    """
    Dessine une étoile fractale de manière récursive.

    :param t: Objet Turtle
    :param length: Longueur des segments
    :param sides: Nombre de branches
    :param depth: Profondeur de récursion
    """
    if depth == 0:
        for _ in range(sides):
            t.forward(length)
            t.right(180 - (360 / sides))
    else:
        for _ in range(sides):
            fractal_star(t, length / 2, sides, depth - 1)
            t.forward(length)
            t.right(180 - (360 / sides))



# Test local
if __name__ == "__main__":
    generate_pattern(
        sides=6,
        depth=15,
        size=120,
        angle=15,
        color='green',
        pattern_type='polygon',
        output_path='static/images/test_pattern.png'
    )
