from math import log10, pow
import numpy as np
import cv2
from skimage.metrics import structural_similarity as SSIM
image_size = 512*512
def Eval(original, denoised):
    MSE = np.mean(original - denoised)
    psnr = 10*log10(pow(255.0, 2)/MSE)
    pixel_range = denoised.max() - denoised.min()
    ssim = SSIM(im1=original, im2=denoised, win_size=3, data_range=pixel_range)
    return psnr, MSE, ssim

orig_img = cv2.imread("Lena.bmp")
mean_gauss_img = cv2.imread("Lena_mean_gauss.bmp")
mean_impulse_img = cv2.imread("Lena_mean_impulse.bmp")
mean_poisson_img = cv2.imread("Lena_mean_poisson.bmp")
median_gauss_img = cv2.imread("Lena_med_gauss.bmp")
median_impulse_img = cv2.imread("Lena_med_impulse.bmp")
median_poisson_img = cv2.imread("Lena_med_poisson.bmp")
bila_gauss_img = cv2.imread("Lena_bilateral_gauss.bmp")
bila_impulse_img = cv2.imread("Lena_bilateral_impulse.bmp")
bila_poisson_img = cv2.imread("Lena_bilateral_poisson.bmp")

denoised_img = [mean_gauss_img, mean_impulse_img, mean_poisson_img,
                median_gauss_img, median_impulse_img, median_poisson_img,
                bila_gauss_img, bila_impulse_img, bila_poisson_img
                ]

noise = ['Gaussian', 'Salt and Pepper', 'Poisson']
eval_mean = []
eval_median = []
eval_bilateral = []
for i in range(3):
    eval_mean.append(Eval(original=orig_img, denoised=denoised_img[i]))
    eval_median.append(Eval(original=orig_img, denoised=denoised_img[i+3]))
    eval_bilateral.append(Eval(original=orig_img, denoised=denoised_img[i+6]))

print("PSNR Evaluation Metric")
for i in range(3):
    print(f"Mean filter for {noise[i]} noise: {eval_mean[i][0]: .4f}")
    print(f"Median filter for {noise[i]} noise: {eval_median[i][0]: .4f}")
    print(f"Bilateral filter for {noise[i]} noise: {eval_bilateral[i][0]: .4f}")

print("\nMSE Evaluation Metric")
for i in range(3):
    print(f"Mean filter for {noise[i]} noise: {eval_mean[i][1]: .4f}")
    print(f"Median filter for {noise[i]} noise: {eval_median[i][1]: .4f}")
    print(f"Bilateral filter for {noise[i]} noise: {eval_bilateral[i][1]: .4f}")

print("\nSSIM Evaluation Metric")
for i in range(3):
    print(f"Mean filter for {noise[i]} noise: {eval_mean[i][2]: .4f}")
    print(f"Median filter for {noise[i]} noise: {eval_median[i][2]: .4f}")
    print(f"Bilateral filter for {noise[i]} noise: {eval_bilateral[i][2]: .4f}")

