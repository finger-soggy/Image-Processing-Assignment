import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("Lena.bmp", 0)
gauss_img = cv2.imread("Lena_Gaussian.bmp", 0)
impulse_img = cv2.imread("Lena_Impulse.bmp", 0)
poisson_img = cv2.imread("Lena_poisson.bmp", 0)
# Assume sigmaColor = sigmaNoise*3
# SigmaSpace is estimated using kernel size
noise_gauss = gauss_img - img
noise_impulse = impulse_img - img
noise_poisson = poisson_img - img
std_gauss = np.std(noise_gauss)
std_impulse = np.std(noise_impulse)
std_poisson = np.std(noise_poisson)
sigmaSpace = 1
sigmaColor_gauss = 3*std_gauss
sigmaColor_impulse = 3*std_impulse
sigmaColor_poisson = 3*std_poisson
bila_gauss = cv2.bilateralFilter(gauss_img, d=5, sigmaColor=sigmaColor_gauss, sigmaSpace=sigmaSpace)
bila_impulse = cv2.bilateralFilter(impulse_img, d=5, sigmaColor=sigmaColor_impulse, sigmaSpace=sigmaSpace)
bila_poisson = cv2.bilateralFilter(poisson_img, d=5, sigmaColor=sigmaColor_poisson, sigmaSpace=sigmaSpace)
cv2.imwrite("Lena_bilateral_gauss.bmp", bila_gauss)
cv2.imwrite("Lena_bilateral_impulse.bmp", bila_impulse)
cv2.imwrite("Lena_bilateral_poisson.bmp", bila_poisson)
plt.figure(figsize=(12, 6))
plt.subplot(131), plt.imshow(bila_gauss, cmap='gray'), plt.title("Gaussian Noise")
plt.subplot(132), plt.imshow(bila_impulse, cmap='gray'), plt.title("Salt and Pepper Noise")
plt.subplot(133), plt.imshow(bila_poisson, cmap='gray'), plt.title("Poisson Noise")
plt.show()