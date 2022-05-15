import PIL
from PIL import Image
import os


width = 1080
source = "input/"
destination = "output/"

# this is the main working code of ths compressor
def resize_pic(old_pic, new_pic, width):
    img = Image.open(old_pic)
    wpercent = (width/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((width,hsize), PIL.Image.ANTIALIAS)
    img.save(new_pic)


def entire_directory(source, destination, width):
    files = os.listdir(source)

    i = 0
    for file in files:
        i+=1
        old_pic = source + "/" +file
        new_pic = destination + "/" +file
        resize_pic(old_pic, new_pic, width)
        print(i, "image compressed")


entire_directory(source, destination, width)
