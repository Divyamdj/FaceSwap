from PIL import Image, ImageChops
import os

path = r'E:/Kroop AI/horse2zebra/downloads/em_final/'
for pic in os.listdir(path):
  filename = path+pic
  im = Image.open(filename)

  #remove white margins
  bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
  diff = ImageChops.difference(im, bg)
  diff = ImageChops.add(diff, diff, 2.0, -100)
  bbox = diff.getbbox()
  if bbox:
    im = im.crop(bbox)
  
  #resize image
  a,b=im.size

  resized_image = im.resize((int(a*0.6),int(b*0.6)))
  resized_image.save(filename)