import cv2
cap=cv2.VideoCapture(0)



while True:
    ret,frame=cap.read()
    cv2.imshow("image",frame)


    lap=cv2.Laplacian(frame,cv2.CV_64F)
    canny=cv2.Canny(frame,100,200)
    cv2.imshow("canny",canny)
    cv2.imshow("laplacian",lap)




    if cv2.waitKey(5)==ord("x"):
        break



cap.release()
cv2.destroyAllWindows()




