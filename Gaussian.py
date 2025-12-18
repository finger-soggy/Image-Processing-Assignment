import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Lena.bmp", 0)
print(img.shape)

gaussian = np.zeros((512, 512), dtype=np.uint8)
cv2.randn(gaussian, 100, 50)
noisy_img = cv2.add(img, gaussian)
cv2.imwrite(r'Lena_Gaussian.bmp', noisy_img)
'''
cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Noise Image", noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title("Original Image")
plt.subplot(122), plt.imshow(noisy_img, cmap='gray'), plt.title("Gaussian Noise Added")
plt.show()

'''
fig=plt.figure(dpi=1000)

fig.add_subplot(1,3,1)
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.title("Original")

fig.add_subplot(1,3,2)
plt.imshow(gaussian, cmap='gray')
plt.axis("off")
plt.title("Gaussian Noise")

fig.add_subplot(1,3,3)
plt.imshow(noisy_img, cmap='gray')
plt.axis("off")
plt.title("Combined")
'''
