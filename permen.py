import cv2
import numpy as np

# Fungsi untuk mengambil laplacian dari gambar yang dihaluskan gaussian (LoG)
def laplacian_of_gaussian(img, ksize):
    img_blur = cv2.GaussianBlur(img, (ksize, ksize), 0)
    img_log = cv2.Laplacian(img_blur, cv2.CV_64F)
    return img_log

# Fungsi untuk mengambil selisih dua gambar yang dihaluskan gaussian (DoG)
def difference_of_gaussian(img, ksize1, ksize2):
    img_blur1 = cv2.GaussianBlur(img, (ksize1, ksize1), 0)
    img_blur2 = cv2.GaussianBlur(img, (ksize2, ksize2), 0)
    img_dog = img_blur1 - img_blur2
    return img_dog

# Fungsi untuk mengambil nilai maksimum dalam matriks determinan Hessian (DoH)
def determinant_of_hessian(img, ksize):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hessian_matrix = cv2.cornerHarris(img_gray, ksize, 3, 0.04)
    return hessian_matrix

# Load citra
img = cv2.imread('python/perment.jpg')

# Set parameter kernel size
ksize_log = 5
ksize1_dog = 3
ksize2_dog = 7
ksize_doh = 5

# Proses pengolahan citra
img_log = laplacian_of_gaussian(img, ksize_log)
img_dog = difference_of_gaussian(img, ksize1_dog, ksize2_dog)
img_doh = determinant_of_hessian(img, ksize_doh)

# Tampilkan citra hasil
cv2.imshow('Laplacian of Gaussian (LoG)', img_log)
cv2.imshow('Difference of Gaussian (DoG)', img_dog)
cv2.imshow('Determinant of Hessian (DoH)', img_doh)

# Tunggu tombol key
cv2.waitKey(0)
cv2.destroyAllWindows()
