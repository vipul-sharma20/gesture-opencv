import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh1 = cv2.threshold(blur,60,255, \
            cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow('thres1', thresh1)
    contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE, \
            cv2.CHAIN_APPROX_SIMPLE)
    #cv2.imshow('thresh2', hierarchy)
    max_area = -1
    for i in range(len(contours)):
        cnt=contours[i]
        area = cv2.contourArea(cnt)
        if(area>max_area):
            max_area=area
            ci=i
    cnt=contours[ci]
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(img.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
    cv2.drawContours(drawing,[hull],0,(0,0,255),2)
    #cv2.imshow('drw', drawing)
    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)
    moments = cv2.moments(cnt)
    if moments['m00']!=0:
        cx = int(moments['m10']/moments['m00']) # cx = M10/M00
        cy = int(moments['m01']/moments['m00']) # cy = M01/M00
    centr=(cx,cy)
    mind = 0
    maxd = 0
    i = 0
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        dist = cv2.pointPolygonTest(cnt,centr,True)
        cv2.line(img,start,end,[0,255,0],2)
        cv2.circle(img,far,5,[0,0,255],-1)
        print i
    cv2.imshow('drawing', drawing)
    #cv2.imshow('thresholded', thresh1)
    #cv2.imshow('blurred', blur)
    cv2.imshow('original', img)
    k = cv2.waitKey(10)
    if k == 27:
        break
