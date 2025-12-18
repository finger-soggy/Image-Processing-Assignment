import cv2
from matplotlib import pyplot as plt

gauss_img = cv2.imread("Lena_Gaussian.bmp", 0)
impulse_img = cv2.imread("Lena_Impulse.bmp", 0)
poisson_img = cv2.imread("Lena_poisson.bmp", 0)

med_gauss = cv2.medianBlur(gauss_img, 5)
med_impulse = cv2.medianBlur(impulse_img, 5)
med_poisson = cv2.medianBlur(poisson_img, 5)
cv2.imwrite("Lena_med_gauss.bmp", med_gauss)
cv2.imwrite("Lena_med_impulse.bmp", med_impulse)
cv2.imwrite("Lena_med_poisson.bmp", med_poisson)
plt.figure(figsize=(12, 6))
plt.subplot(131), plt.imshow(med_gauss, cmap='gray'), plt.title("Gaussian Noise")
plt.subplot(132), plt.imshow(med_impulse, cmap='gray'), plt.title("Salt and Pepper Noise")
plt.subplot(133), plt.imshow(med_poisson, cmap='gray'), plt.title("Poisson Noise")
plt.show()