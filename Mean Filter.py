import cv2
from matplotlib import pyplot as plt

gauss_img = cv2.imread("Lena_Gaussian.bmp", 0)
impulse_img = cv2.imread("Lena_Impulse.bmp", 0)
poisson_img = cv2.imread("Lena_poisson.bmp", 0)

mean_gauss = cv2.blur(gauss_img, (5,5))
mean_impulse = cv2.blur(impulse_img, (5,5))
mean_poisson = cv2.blur(poisson_img, (5,5))
cv2.imwrite("Lena_mean_gauss.bmp", mean_gauss)
cv2.imwrite("Lena_mean_impulse.bmp", mean_impulse)
cv2.imwrite("Lena_mean_poisson.bmp", mean_poisson)
plt.figure(figsize=(12, 6))
plt.subplot(131), plt.imshow(mean_gauss, cmap='gray'), plt.title("Gaussian Noise")
plt.subplot(132), plt.imshow(mean_impulse, cmap='gray'), plt.title("Salt and Pepper Noise")
plt.subplot(133), plt.imshow(mean_poisson, cmap='gray'), plt.title("Poisson Noise")
plt.show()