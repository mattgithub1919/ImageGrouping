import os
import shutil
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from collections import Counter


from CreateDirectory import create_dir
from DeleteDirectory import del_dir
from DeleteHidden import del_hidden
from ReadImage import read_image
from DominantColor import get_dominant_color
from Category import get_category

## Preparation:
#  1. delete unwanted files or folder (there will be unwanted files \\
#     and folders) if the program is run more than once. Users should \\
#     make sure there're no other unwanted files or folders.
#  2. create new category folder
filespath = input('Please input the location of the images: ')
del_dir(filespath)
pic_list = os.listdir(filespath)
clean_pic_list = del_hidden(pic_list)
create_dir(filespath)

## create global variables and customized data structures
pixel_data = dict()
image_group = {'red':{}, 'green':{}, 'blue':{}, 'other':{},}
size = []
sorted_list = []

## read image into customized data structures, namely pixel_data and image_group
for i in range(len(clean_pic_list)):
    pic_color = read_image(clean_pic_list[i])
    # RGB color data is saved for future export
    pixel_data[clean_pic_list[i]] = pic_color
    # area is named size here, it's also saved for future renaming
    size[i] = pic_color.shape[0] * pic_color.shape[1]
    # flatten pixels for dominant color calculation
    pic_color_reshape = pic_color.reshape((size[i], 3))
    dominant_color = get_dominant_color(pic_color_reshape, k = 3)
    category = get_category(dominant_color)
    # pair image name and area with relevant category
    image_group[category].update({clean_pic_list[i]:size[i]})


## sort, rename and export images
for category in image_group.keys():
    # sort each category based on the dictionary values, namely area/size
    sorted_list = sorted(image_group[category].items(), key=lambda (k, v): v, reverse = False)
    # rename each sorted image
    for i in range(len(sorted_list)):
        pic_rename = str(i+1) + '_' + str(size[i]) + '.jpeg'
        save_path = os.path.join(filespath, category, pic_rename)
        # sorted_list[i][0] is image's original name which will \\
        # help find its RGB data in pixel_data
        image_pixel = pixel_data[sorted_list[i][0]]
        im = Image.fromarray(image_pixel)
        im.save(save_path)


