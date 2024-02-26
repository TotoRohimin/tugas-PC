import cv2
import matplotlib.pyplot as plt
import numpy as np

def hitung_histogram(citra):
    # Inisialisasi array histogram
    histogram = np.zeros(256, dtype=int)

    # Menghitung frekuensi setiap nilai keabuan
    for nilai in citra.flatten():
        histogram[nilai] += 1

    return histogram

def tampilkan_histogram(histogram):
    plt.bar(range(256), histogram, color='gray', alpha=0.7)
    plt.title('Histogram Citra Keabuan')
    plt.xlabel('Nilai Keabuan')
    plt.ylabel('Frekuensi')
    plt.savefig('histogram.png') # Simpan histogram sebagai file gambar
    plt.show()

# Mencoba membaca citra
try:
    citra = cv2.imread('python/captured_image.jpg', cv2.IMREAD_GRAYSCALE)

    # Memastikan citra berhasil dibaca
    if citra is None:
        print("Gagal membaca citra.")
    else:
        # Hitung histogram
        histogram = hitung_histogram(citra)

        # Tampilkan citra
        cv2.imshow('Citra Keabuan', citra)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Tampilkan histogram
        tampilkan_histogram(histogram)

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
