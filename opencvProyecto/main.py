import cv2

# read image
img = cv2.imread("images/cat.jpg")

# convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# write image on disk
cv2.imwrite("gray.jpg", gray)

# print(img.shape)

# alto, ancho, dimension
# (557, 983, 3)
