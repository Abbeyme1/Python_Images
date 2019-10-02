# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 00:48:03 2019

@author: Abhay
"""


import numpy as np
from PIL import Image


#width=5
#height=4
#array=np.zeros([height,width,3],dtype=np.uint8)


array=np.zeros([100,250,3],dtype=np.uint8)
array[:,:150]=[255,128,0]
array[:,100:]=[0,0,255]
img=Image.fromarray(array)
img.save('map-img.png')
