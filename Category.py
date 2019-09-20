# get the category of dominant color

def get_category(dominant_color):
    categories = ['red', 'green', 'blue', 'other']
    if dominant_color[0] < 0:
        return categories[3]
    return categories[np.argmax(dominant_color[:3])]
