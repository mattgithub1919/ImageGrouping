# it returns the RGB value of the dominant color. if its first
# and second dominant colors are grayscale, return [-1, -1, -1]

# Please note the default k is set to 1, need to change the value
# during function call

def get_dominant_color(image, k=1):
    clt = KMeans(n_clusters = k)
    labels = clt.fit_predict(image)
    label_counts = Counter(labels)
    dominant_color_1 = clt.cluster_centers_[label_counts.most_common(1)[0][0]]
    dominant_color_2 = clt.cluster_centers_[label_counts.most_common(2)[1][0]]
    if (dominant_color_1[0] == dominant_color_1[1]) & (dominant_color_1[0] == dominant_color_1[2]):
        if (dominant_color_2[0] == dominant_color_2[1]) & (dominant_color_2[0] == dominant_color_2[2]):
            return [-1, -1, -1]
        else:
            return dominant_color_2
    else:
        return dominant_color_1
