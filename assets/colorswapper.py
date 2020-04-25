import numpy as np
import cv2
import os
from PIL import Image


directory = input("Enter the directory name :")
for filename in os.listdir(directory):
    im = cv2.imread("{}/{}".format(directory, filename))
    im[np.where((im == [30,30,30]).all(axis = 2))] = [79,71,55]
    cv2.imwrite("{}/{}".format(directory, filename), im)
print("Done..")
"""
im = Image.open('ahaha/2_1.PNG')
pix = im.load()
print(pix[1,2])rgb(55,71,79)
"""
