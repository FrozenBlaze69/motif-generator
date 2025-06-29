from flask import Flask, render_template, request
import generator
import random
import os
import glob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    image_path = None

    if request.method == "POST":
        # Récupération des paramètres du formulaire
        sides = int(request.form.get("sides", 3))
        depth = int(request.form.get("depth", 10))
        size = int(request.form.get("size", 100))
        angle = float(request.form.get("angle", 15))
        color = request.form.get("color", "blue")
        pattern_type = request.form.get("pattern_type", "polygon")  # Nouveau paramètre

        # Nettoyage des anciennes images (optionnel mais recommandé)
        for file in glob.glob("static/images/*.png"):
            os.remove(file)

        # Génération d'un nom unique pour l'image
        filename = f"pattern_{random.randint(1000,9999)}.png"
        output_path = os.path.join("static/images", filename)

        # Appel à la fonction de génération
        generator.generate_pattern(
            sides=sides,
            depth=depth,
            size=size,
            angle=angle,
            color=color,
            pattern_type=pattern_type,
            output_path=output_path
        )

        image_path = output_path

    return render_template("index.html", image=image_path)

if __name__ == "__main__":
    app.run(debug=True)
