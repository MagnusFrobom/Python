from PIL import Image
filename = r'Mf-favico.png'
img = Image.open(filename)
img.save('logo.ico')
