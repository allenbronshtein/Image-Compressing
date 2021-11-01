import numpy as np
import matplotlib.pyplot as plt
from sys import argv


# split points into clusters with corresponding centeroids
def cluster(pixels, z, clusters):
    k = len(z)
    for p in pixels:
        min_i = 0
        min_d = float('inf')
        for i in range(0, k):
            d = np.linalg.norm(z[i] - p)
            if d < min_d:
                min_d, min_i = d, i
        clusters[min_i] = np.append(clusters[min_i], p)


# get means of each cluster
def get_means(clusters):
    means = []
    for cluster in clusters:
        if not cluster:
            means.append(NULL)


# update center to be the clusters mean
def fix_center():
    pass


image_fname, centroids_fname, out_fname = 'Image-Compressing/files/dog.jpeg', 'Image-Compressing/files/cents1.txt', 'Image-Compressing/files/out.txt'
z = np.loadtxt(centroids_fname)  # Load centroids
orig_pixels = plt.imread(image_fname)
pixels = (orig_pixels.astype(float) / 255).reshape(-1, 3)
clusters = [np.array([])] * len(z)
cluster(pixels, z, clusters)
print(clusters)
get_means(clusters)
