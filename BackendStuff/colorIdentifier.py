from PIL import Image
import json

input_image = Image.open("screenshot.png")
pixel_map = input_image.load()
width, height = input_image.size


with open('file.json', 'r+') as file:
    # First we load existing data into a dict.
    cords = json.load(file)

print(cords)

