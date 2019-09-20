# ImageGrouping
This serves as a code challenge of FAIMDATA.com
  
## Instructions
Please follow below steps to run this program.
1. Download the zipped images, unzip the images and copy the folder path. Make sure there's no additional files in the folder
2. Download all python files into a different folder. 
3. Run Main.py and paste image folder path when requested. 
4. Categoried images will be sorted, renamed and exported to relevant folders under the image folder

## Resources, libraries used
1. I would like to thank the author of the article below as it I learned the algorithm to calculate dominant color. 
https://adamspannbauer.github.io/2018/03/02/app-icon-dominant-colors/
2. Here's a list of the python 3 libraries used in this program:
  os, 
  shutil, 
  collections,
  numpy = 1.16.2, 
  PIL = 6.1.0, 
  sklearn = 0.20.3, 

## Limitations
Even though the programmer has tried its best, there are still a few limitations
1. image data are saved until the program ends and that might take a lot of storage, especially when the size and number of the images increase. 
2. The program is very contrained to the code challenge and cannot generalize to other image grouping tasks. 
3. The program will clean '.DS_Store' in Mac and 'Thumbs.db' in Windows automatically. The user may need to include relevant system file name in DeleteHidden.py is other Operation Systems are used than Mac and Windows.
4. Some functions can be optimized. Better APIs may exist. 
