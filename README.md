# ImageGrouping
This serves as a code challenge of FAIMDATA.com
  
## Instructions
Please follow below steps to run this program.
1. Download the zipped images, unzip the images and copy the folder path. Make sure there's no additional files in the folder
2. Download all python files into a different folder. 
3. Run Main.py and paste image folder path when requested. 
4. Categoried images will be sorted, renamed and exported to relevant folders under the image folder

## Resources, libraries used
1. Online resources below give me hints and I would like to mention them and thank their authors. <br />
https://adamspannbauer.github.io/2018/03/02/app-icon-dominant-colors/ <br />
https://stackoverflow.com/questions/50331463/convert-rgba-to-rgb-in-python <br />
https://thomas-cokelaer.info/blog/2017/12/how-to-sort-a-dictionary-by-values-in-python/ <br />

2. Here's a list of the python 3 libraries used in this program: <br />
  os, <br />
  shutil, <br />
  collections,<br />
  numpy = 1.16.2, <br />
  PIL = 6.1.0, <br />
  sklearn = 0.20.3, <br />

## Limitations
Even though the programmer has tried its best, there are still a few limitations <br />
1. image data are saved until the program ends and that might take a lot of storage, especially when the size and number of the images increase. 
2. The program is very contrained to the code challenge and cannot generalize to other image grouping tasks. 
3. The program will clean '.DS_Store' in Mac and 'Thumbs.db' in Windows automatically. The user may need to include relevant system file name in DeleteHidden.py is other Operation Systems are used than Mac and Windows.
4. Some functions can be optimized. Better APIs may exist. 
5. It might be possible to use some matrix to replace the loops. That will save time and space. 
5. I can do a time and space complexity analysis here.
6. A proposal to remove pixel_data: dynamic sort. may not be possible.
7. Can make it more encapsulated. Even change data structure implementation, the operation won't change. 
