from PIL import Image
import os

directory = input("Enter the directory name :")
basewidth = int(input("Enter the base width :"))
for filename in os.listdir(directory):
    img = Image.open(directory+"/"+filename)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(directory+"/"+filename) 
    print("Resized " + filename + " ..")
print("Done resizing")
