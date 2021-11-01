import numpy as np
import matplotlib.pyplot as plt
from sys import argv

image_fname, centroids_fname, out_fname = 'Image-Compressing/files/dog.jpeg', 'Image-Compressing/files/cents1.txt', 'Image-Compressing/files/out.txt'
z = np.loadtxt(centroids_fname)  # Load centroids

orig_pixels = plt.imread(image_fname)
plt.show()
pixels = orig_pixels.astype(float) / 255
# Reshape the image (128x128x3) into and Nx3 matrix where N = number of pixels.
pixels = pixels.reshape(-1, 3)
