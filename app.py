# import numpy as np 
# import cv2 
# from cartracking import *
# import streamlit as st
# car_width, car_height = 100, 40
# bike_width, bike_height = 70,30
# car_sensitivity = 500
# bike_sensitivity = 400
# position_path = 'CarParkPos'
# video_path = 'video/CarPark.mp4'
# # video_path = 0s


# # f = st.file_uploader("Upload file")
# if True:
#     # tfile = tempfile.NamedTemporaryFile(delete=False)
#     # tfile.write(f.read())
#     cap = cv2.VideoCapture(video_path)
#     # writer = cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc(*"MJPG"), 30,(1100,720))
#     posList = get_file(position_path)
#     while cap.isOpened():
#         try:
#             status,img = cap.read()
#             img, imgDilate, imgMedian = img_processing(img,status)
#         except:
#             break
#         checkParkingSpace(img,imgDilate,posList,car_width, car_height,bike_width, bike_height,car_sensitivity,bike_sensitivity)
#             # writer.write(img)
#             # cv2.imshow("Image", img)
#             # print(img.shape)
#             # cv2.imshow("ImageThres", imgMedian)
#             # cv2.waitKey(1)   
#     cap.release()
#         # writer.release()
#     cv2.destroyAllWindows()
#         # st.video('output.avi')

import cv2
import streamlit as st
from cartracking import *
st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
car_width, car_height = 100, 40
bike_width, bike_height = 70,30
car_sensitivity = 500
bike_sensitivity = 400
position_path = 'CarParkPos'
posList = get_file(position_path)
while run:
    status, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img, imgDilate, imgMedian = img_processing(frame,status)
    checkParkingSpace(img,imgDilate,posList,car_width, car_height,bike_width, bike_height,car_sensitivity,bike_sensitivity)
    FRAME_WINDOW.image(img)
else:
    st.write('Stopped')