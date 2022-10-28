import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)


#huadongtiao
trackbar_name7="Blur"#降噪
trackbar_name1="interation_dialte"#膨胀迭代次数
trackbar_name2="dilationSize"#膨胀核大小
trackbar_name3="interation_erode"#侵蚀迭代次数
trackbar_name4="erodeSize"#侵蚀核大小
trackbar_name5="threshold"#二值化阈值
win_name="TrackbarDemo"#图像处理

max_num7 = 10
max_num1 = 10
max_num2 = 5
max_num3 = 10
max_num4 = 5
max_num5 = 255
max_num6 = 479

blur_size=0
dialte_value=0
dialte_size = 0
erode_value=0
erode_size = 0
threshold_value=90


max_t1 = 100
max_t2 = 100
max_t3 = 100
max_s1 = 70
asvalue = 20
tlvalue = 40
trvalue = 40
sevalue = 70

line=0
value = 0
value2 = 0
size2 = 0
kerner12=0
value1 = 0
size1 = 0
kerner11=0

def on_blur(arg):
    return cv2.getTrackbarPos(trackbar_name7,win_name)*2+1
def on_threshold(arg):
    pass
def on_erode_and_dialte(arg):
    pass



cv2.namedWindow(win_name)
cv2.createTrackbar(trackbar_name7,win_name,blur_size,max_num7,on_blur)
cv2.createTrackbar(trackbar_name1,win_name,dialte_value,max_num1,on_erode_and_dialte)
cv2.createTrackbar(trackbar_name2,win_name,dialte_size,max_num2,on_erode_and_dialte)
cv2.createTrackbar(trackbar_name3,win_name,erode_value,max_num3,on_erode_and_dialte)
cv2.createTrackbar(trackbar_name4,win_name,erode_size,max_num4,on_erode_and_dialte)
cv2.createTrackbar(trackbar_name5,win_name,threshold_value,max_num5,on_threshold)

def tuxiang():
    i=1
    while( 1 ):
        #USB摄像头工作时,读取一帧图像
        #ret, frame = cap.read()
        #显示图像窗口在树莓派的屏幕上
        #cv2.imshow('frame',frame)
        # 转化为灰度图
        gray =cv2.imread('caochang.jpg',cv2.IMREAD_GRAYSCALE)
        # 大津法二值化
        value = cv2.getTrackbarPos(trackbar_name5,win_name)
        retval, dst = cv2.threshold(gray, value, 255, cv2.THRESH_BINARY)
        dst=cv2.medianBlur(dst,on_blur(0))
        #膨胀侵蚀
        value2 = cv2.getTrackbarPos(trackbar_name3,win_name)
        size2 = cv2.getTrackbarPos(trackbar_name4,win_name)
        kerner12=cv2.getStructuringElement(cv2.MORPH_RECT,(2*size2+1,2*size2+1))
        res = cv2.erode(dst,kerner12,None,None,value2)
        
        value1 = cv2.getTrackbarPos(trackbar_name1,win_name)
        size1 = cv2.getTrackbarPos(trackbar_name2,win_name)
        kerner11=cv2.getStructuringElement(cv2.MORPH_RECT,(2*size1+1,2*size1+1))   
        res = cv2.dilate(res,kerner11,None,None,value1)
        cv2.imshow(win_name,res)
        #按下w键退出
        key = cv2.waitKey(1)
        #print( '%08X' % (key&0xFFFFFFFF) )
        if key & 0x00FF  == ord('s'):
            cv2.imwrite('p'+str(i)+'.jpg',res)
            i+=1
        if key & 0x00FF  == ord('q'):
            break

tuxiang()
# 释放资源和关闭窗口

cap.release()
cv2.destroyAllWindows()

