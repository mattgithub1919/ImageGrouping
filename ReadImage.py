# read image
# 1. '.png' format has 4(RGBA) columns of color data and \\
#   need to change to 3 (RGB)

def read_image(image_filename):
    global filespath
    
    image_path = os.path.join(filespath, image_filename)
    # RGBA data obtained
    image_color = np.array(Image.open(image_path))
    # image_color = np.array(image_color_RGBA.convert('RGB'))
    return image_color

