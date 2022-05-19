import cv2

img = cv2.imread('C:\\Users\\melik\\Desktop\\girlimage.jpeg')
cv2.imshow('Original image', img)

b,g,r = cv2.split(img)
cv2.imshow("Model Blue Image", b)
cv2.imshow("Model Green Image", g)
cv2.imshow("Model Red Image", r)

for row in range(0,img.shape[0]):
    for col in range(0,img.shape[1]):
        if b[row,col] > 100:
            b[row,col] = 20

merged_image = cv2.merge([b,g,r])
cv2.imshow("Merged Image", merged_image)

cv2.waitKey(0)
