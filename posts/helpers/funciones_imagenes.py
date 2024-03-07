from PIL import Image

def redimensionar_imagen(imagen, ancho, alto):
    img = Image.open(imagen)
    img = img.resize((ancho, alto), Image.ANTIALIAS)
    return img
