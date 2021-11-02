import numpy as np
import matplotlib.pyplot as plt
from sys import argv

APPEND = 0
FLUSH = 1


# split points into clusters with corresponding centeroids
def cluster_points(pixels, z):
    k = len(z)
    clusters = [np.empty(shape=[0, 3])] * k
    for p in pixels:
        min_i, min_d = 0, float('inf')
        for i in range(k):
            d = np.linalg.norm(z[i] - p)
            if d < min_d: min_d, min_i = d, i
        clusters[min_i] = np.append(clusters[min_i], [p], axis=0)
    return clusters


# get means of each cluster
def get_means(clusters):
    k = len(clusters)
    means = np.array([]).reshape(0, 3)
    for cluster in clusters:
        size = cluster.size
        if size:
            means = np.append(means, [(cluster.sum(axis=0) / size)], axis=0)
        else:
            means = np.append(means, None, axis=0)
    return means


# update center to be the clusters mean
def fix_center(z, means):
    k = len(z)
    for i in range(k):
        if means[i] is not None: z[i] = means[i]


# log centroids in out file
def logger(z, out):
    log_body = ''
    _out = out

    def log(z, cmd):
        s = ''
        nonlocal log_body
        for _z in z:
            s += f'{_z},'
        log_body += f"[iter {i}]:{s[:-1]}\n"
        print(log_body)
        if cmd == 1:
            _out.write(log_body)
            log_body = ''
            _out.close()

    return log


# Main
orig_pixels = plt.imread('Image-Compressing/files/dog.jpeg')
pixels = (orig_pixels.astype(float) / 255).reshape(-1, 3)
z = np.loadtxt('Image-Compressing/files/cents1.txt').round(4)
out = open('Image-Compressing/files/test.txt', "a")
logger = logger(z, out)

for i in range(20):
    logger(z, APPEND)
    clusters = cluster_points(pixels, z)
    means = get_means(clusters).round(4)
    if not np.array_equal(z, means): fix_center(z, means)
    else: break
logger(z, FLUSH)
