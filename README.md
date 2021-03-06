# ImageGrouping
Given 50 images of various dimensions, the main goal is to classify images by dominant color into read, green, blue and other groups. Images need to be sorted, exported and renamed based on their rank.
  
## Instructions
### Please follow below steps to run this program.
1. Download the zipped images, unzip the images and copy the folder path. Make sure there's no additional files the first time the program is run. 
    * Any non-image file in the folder will cause "OSError" during read_image function running. 
    * However, there's no need to delete program-created folders if the program is run more than once. 
    * An example of copied image folder path could be, /Users/yang/Desktop/images
2. Download the zipped files, unzip and save into a different folder from the image folder. 
3. Run **Main.py** and paste above image folder path when requested. Leave the program running.
    * Python libraries mentioned below should be installed before running this program.
4. Categoried images will be sorted, renamed and exported to relevant folders under the image folder

## Resources, libraries used
### 1. Online resources below give me hints and I would like to mention them and thank their authors. <br />
    * https://adamspannbauer.github.io/2018/03/02/app-icon-dominant-colors/
    * https://stackoverflow.com/questions/50331463/convert-rgba-to-rgb-in-python
    * https://thomas-cokelaer.info/blog/2017/12/how-to-sort-a-dictionary-by-values-in-python/

### 2. Here's a list of the python 3 libraries used in this program: <br />
    * os
    * shutil
    * collections
    * numpy = 1.16.2
    * PIL = 6.1.0
    * sklearn = 0.20.3

## Limitations
Even though the programmer has tried its best, there are still a few limitations:

1. The variable _pixel_data_ is saved until the program ends and that takes up storage, especially when the size and number of the images increase. 
    *  Improvement: one possible solution is to export image with original filename and use dictionary to pair its original name and final sorted name. Then change name in the final step.<br />

2. The program is made for the code challenge and need to make changes to generalize to other image grouping tasks. <br />

3. The program will clean _'.DS_Store'_ in Mac and _'Thumbs.db'_ in Windows automatically. The user may need to include relevant system file name in DeleteHidden.py if other Operation System is used.The user cannot add any additional file in the folder.<br />

4. This program is not well encapsulated. Further encapsulation will allow the data structure implementation to change while the program is not disturbed. <br />

5. A few optimization tips:
    *  Faster APIs may be used to replace current code. 
    *  Use faster matrix(i.e. Numpy array) to replace the loops. That will save time and space.
    *  Use ImageNet to obtain more effective features and improve image-grouping accuracy.

