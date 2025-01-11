# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.JPG'
NEW_IMAGE = ROOT_FOLDER / 'New.JPG'

pil_image = Image.open(ORIGINAL) # Abrir a imagem
width, height = pil_image.size # Joga os valores de altura e largura nas váriavels
exif = pil_image.info['exif'] # Salva as informações de data, hora, qual a camera, etc...

# print(pil_image.size) # Retorna a lagura e altura

# Regra de três para ter a porção correta de altura
# width     new_width
# height    X
new_width = 640 # Pixels de largura
new_height = round(height * new_width / width) # Faz o calculo da altura e arrendonda o valor
print(width, height)
print(new_width, new_height)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE, # Caminho da nova imagem
    optimize=True, # Otimização 
    quality=90, # Porcentagem de qualidade
    exif=exif,
)