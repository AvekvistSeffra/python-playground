import random

recipe = []

with open("recipe.txt") as f:
    recipe = f.read().lower().split(" ")

random.shuffle(recipe)

recipe = " ".join(recipe)

with open("processed_recipe.txt") as f:
    f.write(recipe)
