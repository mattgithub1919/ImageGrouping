# read image
# 1. '.png' format has 4(RGBA) columns of color data and \\
#   need to change to 3 (RGB)

def read_image(image_filename):
    global pixel_data
    global image_group
    global filespath
    
    image_path = os.path.join(filespath, image_filename)
    # RGBA data obtained
    image_color_RGBA = Image.open(image_path)
    # Change RGBA data into RGB
    # it's possible not to change. That will be a different solution
    image_color = np.array(image_color_RGBA.convert('RGB'))
    return image_color
