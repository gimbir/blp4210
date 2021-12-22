# OpenCv kullanarak bir görüntü okuyun, görüntüyü siyah beyaz cevirin gösterin, filtre kullanarak: gaussian blur , canny kenar bulma, keskinleştirme filtresi(   ), sobel filtresi(       ), ortalama blur filtresi(  ) , Laplacian filtresi , dilation işlemi, erosion işlemi, olacak şekilde 8 işlemi, subplot kullanarak çizdirin. Görüntünün histogramını çıkarıp çizdirin, threshold  belirleyip, objeleri siyah-beyaz gösterin(basit segmentasyon) yapın
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('animals.jpg')
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('Original', img)
plt.subplot(1, 1, 1), plt.imshow(rgb_img, 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.show()

# Siyah Beyaz
gray = cv.cvtColor(rgb_img, cv.COLOR_BGR2GRAY)
# cv.imshow('Black and White', gray)
plt.subplot(1, 1, 1), plt.imshow(gray, 'gray')
plt.title('Black and White'), plt.xticks([]), plt.yticks([])
plt.show()

# GaussianBlur
blur = cv.GaussianBlur(rgb_img, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)
plt.subplot(1, 1, 1), plt.imshow(blur, 'gray')
plt.title('GaussianBlur'), plt.xticks([]), plt.yticks([])
plt.show()

# Canny Edges
canny = cv.Canny(rgb_img, 125, 175)
# cv.imshow('Canny Edges', canny)
plt.subplot(1, 1, 1), plt.imshow(canny, 'gray')
plt.title('Canny Edges'), plt.xticks([]), plt.yticks([])
plt.show()

# Sharpening
sharp_filter = np.array(
    [
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0],
    ]
)

sharp_img = cv.filter2D(rgb_img, -1, sharp_filter)

plt.subplot(1, 1, 1), plt.imshow(sharp_img, 'gray')
plt.title('Sharpened'), plt.xticks([]), plt.yticks([])
plt.show()

# cv.imshow('Sharpened', sharp_img)
# cv.waitKey(0)
# cv.destroyAllWindows()


# # Sobel
sobelx = cv.Sobel(rgb_img, cv.CV_64F, 1, 0)
sobely = cv.Sobel(rgb_img, cv.CV_64F, 0, 1)

plt.subplot(2, 2, 1), plt.imshow(rgb_img, 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 3), plt.imshow(sobelx, 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# cv.imshow('Sobel X', sobelx)

plt.subplot(2, 2, 4), plt.imshow(sobely, 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# cv.imshow('Sobel Y', sobely)
plt.show()

# Average Blur
kernel = np.ones((5, 5), np.float32) / 9
dst = cv.filter2D(rgb_img, -1, kernel)

plt.subplot(1, 2, 1), plt.imshow(rgb_img, 'gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])


plt.subplot(1, 2, 2), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
# cv.imshow('Median Blur', dst)

plt.show()

# Laplacion
laplacion = cv.Laplacian(rgb_img, cv.CV_64F)
plt.subplot(1, 1, 1), plt.imshow(laplacion, 'gray'), plt.title('Laplacion')
plt.xticks([]), plt.yticks([])
# cv.imshow('Laplacion', laplacion)

plt.show()

# Dilation
dilated = cv.dilate(canny, (7, 7), iterations=1)
plt.subplot(1, 1, 1), plt.imshow(dilated, 'gray'), plt.title('Dilation')
plt.xticks([]), plt.yticks([])
# cv.imshow('Dilation', dilated)
plt.show()

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
plt.subplot(1, 1, 1), plt.imshow(eroded, 'gray'), plt.title('Eroding')
plt.xticks([]), plt.yticks([])
# cv.imshow('Eroding', eroded)
plt.show()

# Histogram
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv.calcHist([rgb_img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.hist(rgb_img.ravel(), 256, [0, 256])
plt.show()

# Threshold
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
plt.subplot(1, 1, 1), plt.imshow(thresh, 'gray'), plt.title('Threshold')
plt.xticks([]), plt.yticks([])
# cv.imshow('Threshold', thresh)
plt.show()

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
plt.subplot(1, 1, 1), plt.imshow(thresh_inv, 'gray'), plt.title('Threshold Inverted')
plt.xticks([]), plt.yticks([])
# cv.imshow('Threshold Inverted', thresh_inv)
plt.show()

# Adaptive Threshold
adaptive_threshold = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3
)
plt.subplot(1, 1, 1), plt.imshow(adaptive_threshold, 'gray'), plt.title(
    'Adaptive Threshold'
)
plt.xticks([]), plt.yticks([])
# cv.imshow('Adaptive Threshold', adaptive_threshold)
plt.show()
