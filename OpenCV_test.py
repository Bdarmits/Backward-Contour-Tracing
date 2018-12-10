# Contour Approximation OpenCV algorithm Алгоритм Кенні Ramer–Douglas–Peucker algorithm
import cv2
def opencv_contour_approx(name):
    # name = "test_image_03.png"
    img1 = cv2.imread(name)
    img2 = img1
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(img2,100,200)
    (_ ,cnts,_ ) = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cnt = cnts[0]
    epsilon = 0.001*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    cv2.drawContours(img1,[approx],-1,(0,255,0),3)
    cv2.imwrite('rezults\{}_OpenCVrezult.png'.format(name),img1)
    cv2.imshow(name + "_rezult",img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

