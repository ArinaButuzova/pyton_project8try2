from PIL import Image

image = Image.open('bears.jpg')
cropped = image.crop((0, 0, 921, 1268))
cropped.save('bear.jpg')
cropped.show()








