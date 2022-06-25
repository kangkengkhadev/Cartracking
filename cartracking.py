#import libraries
import pickle
import cvzone
import numpy as np
import cv2

#define 
# car_width, car_height = 100, 40
# bike_width, bike_height = 70,30
# car_sensitivity = 500
# bike_sensitivity = 400
# position_path = 'video/CarParkPos'
# video_path = 'video/CarPark.mp4'

#start video
def get_file(position_path):
    with open(position_path, 'rb') as f:
        posList = pickle.load(f)
    return posList

#checkParkingSpace
def checkParkingSpace(img,imgPro,posList,car_width, car_height,bike_width, bike_height,car_sensitivity,bike_sensitivity):
    car_all = 0
    bike_all = 0
    car_count = 0
    bike_count = 0
    for pos in posList:
        x, y = pos[0]
        if pos[1] == 'car':
            imgCrop = imgPro[y:y + car_height, x:x + car_width]
        elif pos[1] == 'bike':
            imgCrop = imgPro[y:y + bike_height, x:x + bike_width]
        count = cv2.countNonZero(imgCrop)
        
        #car        
        if pos[1] == 'car':
            car_all+=1
            if count < car_sensitivity:
                color = (0, 255, 0)
                thickness = 1
                car_count += 1
            else:
                color = (0, 0, 255)
                thickness = 1
            width = car_width
            height = car_height 
            
        #bike
        elif pos[1] == 'bike':
            bike_all += 1
            if count < bike_sensitivity:
                color = (0, 255, 0)
                thickness = 1
                bike_count += 1
            else:
                color = (0, 0, 255)
                thickness = 1
            width = bike_width
            height = bike_height   
        #rectangle
        cv2.rectangle(img, pos[0], (pos[0][0] + width, pos[0][1] + height), color, thickness)
        cvzone.putTextRect(img, f'{pos[1]} and {str(count)}', (x, y + height - 3), scale=1,
                            thickness=2, offset=0, colorR=color)
    #title
    cvzone.putTextRect(img, f'CarFree: {car_count}/{car_all} BikeFree: {bike_count}/{bike_all}', (100, 50), scale=1,
                           thickness=2, offset=20, colorR=(0,200,0))
    
#preprocess image
def img_processing(img,status):  
    
    if status == True:
        #imgprocessing
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)
        return img, imgDilate, imgMedian
    
#start running
# cap,posList = get_file(video_path,position_path)
# while cap.isOpened():
#     try:
#         img, imgDilate, imgMedian = img_processing(cap)
#     except:
#         break
#     checkParkingSpace(img,imgPro,posList,car_width, car_height,bike_width, bike_height,car_sensitivity,bike_sensitivity)
#     cv2.imshow("Image", img)
#     print(img.shape)
#     cv2.imshow("ImageThres", imgMedian)
#     cv2.waitKey(1)