import numpy as np
import cv2
import matplotlib.pyplot as plt
import random

def add_salt_and_pepper_noise(image, prob=0.05):
    noisy_image = image.copy()
    num_salt = int(prob * image.size * 0.5)
    num_pepper = int(prob * image.size * 0.5)
    for i in range(num_salt):
        y = random.randint(0, 511)
        x = random.randint(0, 511)
        noisy_image[y][x] = 255
    for i in range(num_pepper):
        y = random.randint(0, 511)
        x = random.randint(0, 511)
        noisy_image[y][x] = 0

    return noisy_image

img = cv2.imread("Lena.bmp", 0)
print(img.shape)

noisy_img = add_salt_and_pepper_noise(img)
cv2.imwrite("Lena_Impulse.bmp", noisy_img)
'''
imp_noise = np.zeros((512, 512), dtype=np.uint8)
cv2.randu(imp_noise, 0, 255)
imp_noise = cv2.threshold(imp_noise, 240, 255, cv2.THRESH_BINARY)[1]
noisy_img = cv2.add(img, imp_noise)
cv2.imwrite(r'Lena_Impulse.bmp', noisy_img)
'''
plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title("Original Image")
plt.subplot(122), plt.imshow(noisy_img, cmap='gray'), plt.title("Salt and Pepper Noise Added")
plt.show()