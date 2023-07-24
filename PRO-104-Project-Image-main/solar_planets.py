import cv2
img=cv2.imread("solar-system.jpg")


cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
        


)
cv2.putText(img,
            "Mercury",
            (100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
        


)
cv2.putText(img,
            "Venus",
            (200,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
        


)
cv2.putText(img,
            "Earth",
            (280,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
        


)
cv2.putText(img,
            "Mars",
            (380,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
        


)
cv2.putText(img,
            "Jupiter",
            (480,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
        


)
cv2.putText(img,
            "saturn",
            (680,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
        


)

cv2.putText(img,
            "Uranus",
            (980,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
        


)
cv2.putText(img,
            "Neptune",
            (1080,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
        


)


cv2.imshow("output",img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg", img)
