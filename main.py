import cv2 #for image processing
import easygui #to open the filebox
import numpy as np #to store image
import imageio #to read image stored at particular path
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

def upload():
    ImagePath=easygui.fileopenbox()
    cartoonify(ImagePath)

def cartoonify(ImagePath):
    originalmage = cv2.imread(ImagePath) # This is for reading image
    originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)

    ReSized1 = cv2.resize(originalmage, (960, 540)) # To bring all the images in a similar size.

    grayScaleImage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2GRAY)# Converting the Image to the gray scale and color
    ReSized2 = cv2.resize(grayScaleImage, (960, 540)) # We do this to ease the computation. So we are working only with blacka nd white

    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5) # Now we need to  create a blurry effect of the image for the noise reduction.
    ReSized3 = cv2.resize(smoothGrayScale, (960, 540))

    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)
    ReSized4 = cv2.resize(getEdge, (960, 540)) # This will give us the output of the edges of an image.

    colorImage = cv2.bilateralFilter(originalmage, 9, 300, 300) # Now we take the original image and make it blur. It is similar to the previous one and takes the smoothing to an extent
    ReSized5 = cv2.resize(colorImage, (960, 540))

    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge) # Now we combine these getedge and colorImage. We just mask the image with the getEdge.
    ReSized6 = cv2.resize(cartoonImage, (960, 540))

    # plt.imshow(ReSized6, cmap='gray')# This will show the image that we have created.





upload()




