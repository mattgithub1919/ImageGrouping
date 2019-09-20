# it returns the RGB value of the dominant color. if its first
# and second dominant colors are greyscale, return [-1, -1, -1, -1]

# Please note the default k is set to 1, need to change the value
# during function call

def get_dominant_color(image, k=1):
    clt = KMeans(n_clusters = k)
    labels = clt.fit_predict(image)
    label_counts = Counter(labels)
    # one example of label_counts is [(0, 126230), (1, 61680), (2, 15040)]
    dominant_color_1 = clt.cluster_centers_[label_counts.most_common(1)[0][0]]
    dominant_color_2 = clt.cluster_centers_[label_counts.most_common(2)[1][0]]
    dominant_color_3 = clt.cluster_centers_[label_counts.most_common(3)[2][0]]
    dominant_color_4 = [-1, -1, -1, -1]
    for item in [dominant_color_1, dominant_color_2, dominant_color_3, dominant_color_4]:
        item = [int(i) for i in item]
        value_diff = (abs(item[0]-item[1]) > 10) and ((abs(item[0]-item[2]) > 10)) \
                     and ((abs(item[1]-item[2]) > 10))
        if value_diff or (item[0] < 0):
            return item
        else:
            continue
