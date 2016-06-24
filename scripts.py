import cv2

for num in range(3, 25):
    img = cv2.imread('imgin/example_{0}_1.jpg'.format(num))
    im = cv2.medianBlur(img, 5)
    height, width, _ = img.shape

    rect = img[0:50, 0:50]
    mean = rect.mean()
    THRESH_METHOD = cv2.THRESH_BINARY if (mean < (255 - mean)) else cv2.THRESH_BINARY_INV

    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(imgray, 127, 255, THRESH_METHOD)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    x1, y1, x2, y2 = width, height, 0, 0
    print num, len(contours)
    for con in contours:
        area = cv2.contourArea(con)
        if area > 10000.0 or len(contours) < 500:
            x, y, w, h = cv2.boundingRect(con)
            x1, y1, x2, y2 = min(x, x1), min(y, y1), max(x + w, x2), max(y + h, y2)
            # img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)

    img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)
    cv2.imwrite('imgout/example_{0}_contour.jpg'.format(num), img)
