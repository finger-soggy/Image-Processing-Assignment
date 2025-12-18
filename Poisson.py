import numpy as np
import cv2
from skimage.util import random_noise
import matplotlib.pyplot as plt

img = cv2.imread("Lena.bmp", 0)
print(img.shape)
noisy_img = np.random.poisson(img/255.0*50) / 50 * 255

cv2.imwrite("Lena_Poisson.bmp", noisy_img)
plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title("Original Image")
plt.subplot(122), plt.imshow(noisy_img, cmap='gray'), plt.title("Poisson Noise Added")
plt.show()
