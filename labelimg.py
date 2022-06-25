#import libraries
import pickle
import cv2
import cvzone
#define 
car_width, car_height = 100, 40
bike_width, bike_height = 70,30
position_path = 'video/CarParkPos'
video_path = 'video/carPark.mp4'

#find img
cap = cv2.VideoCapture(video_path)
i = 0
while True:
    i+=1
    print(i)
    status,image = cap.read()
    if i == 10:
        img = image
        break
    
#debug
try:
    with open(position_path, 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

#function click
def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append([(x, y),'car'])
    if events == cv2.EVENT_RBUTTONDOWN:
        posList.append([(x, y),'bike'])
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

#start running
while True:
    car_count = 0
    bike_count = 0
    for pos in posList:
        if pos[1] == 'car':
            car_count +=1 
            cv2.rectangle(img, pos[0], (pos[0][0] + car_width, pos[0][1] + car_height), (255, 0, 255), 2)
        elif pos[1] == 'bike':
            cv2.rectangle(img, pos[0], (pos[0][0] + bike_width, pos[0][1] + bike_height), (255, 255, 255), 2)    
            bike_count +=1
    cvzone.putTextRect(img, f'Car: {car_count} Bike: {bike_count}', (100, 50), scale=1,
                           thickness=2, offset=20, colorR=(0,200,0))
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)
