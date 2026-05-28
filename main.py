import cv2 as cv
import mediapipe as mp
import mediapipe as mp
import pyautogui 
import numpy as np
import math

clicked = False
screen_w,screen_h =pyautogui.size()
prev_x=0
prev_y=0
prev_x3 = 0
prev_y3=0
x1,y1,x2,y2,x3,y3,x4,y4,x5,y5 =0,0,0,0,0,0,0,0,0,0
prev_scroll=0
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)
mp_draw = mp.solutions.drawing_utils


cap = cv.VideoCapture(0)

while True:
    success, frame =cap.read()
    frame = cv.flip(frame,1)

    rgb =cv.cvtColor(frame,cv.COLOR_BGR2RGB)

    results = hands.process(rgb)


    #if hands detected
    if results.multi_hand_landmarks:
       for hand_landmarks in results.multi_hand_landmarks: 
           mp_draw.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)

       for id,lm in enumerate(hand_landmarks.landmark):
          h,w,c = frame.shape
          cx= int(lm.x*w)
          cy= int(lm.y*h)
          
        #   cv.putText(frame,f"{lm.x},{lm.y}",(cx+20,cy),cv.FONT_HERSHEY_DUPLEX,1.0,(0,255,255),thickness=1)
          if id ==16:
             x4=int(lm.x*w)
             y4= int(lm.y*h)
          if id==4:
              x1= int(lm.x*w)
           
              y1= int(lm.y*h)
          
          if id ==12:
              x3 = int(lm.x*w)
              y3 = int(lm.y*h)

          if id ==20:
             x5=int(lm.x*w)
             y5= int(lm.y*h)

          if id==8:
           curr_x = np.interp(cx,[0,640],[0,screen_w])
           curr_y = np.interp(cy,[0,480],[0,screen_h])

           curr_x = prev_x +(curr_x-prev_x)/5
           curr_y = prev_y+(curr_y-prev_y)/5
           x2 = cx
           y2 = cy
           
           distance2 = math.hypot(x1-x4,y1-y4)
           if distance2<40:
                pyautogui.scroll(30)
              
           distance3 = math.hypot(x1-x5,y1-y5)
           if distance3<40:
            pyautogui.scroll(-30)
            

           if abs(curr_x-prev_x)>2: 
            pyautogui.moveTo(curr_x,curr_y)
           prev_x=curr_x
           prev_y=curr_y

        

          distance1 = math.hypot(x1-x3,y1-y3)
          if distance1 < 55:
             if not clicked:
              pyautogui.click()
              clicked =True
          else:
                clicked = False


    cv.imshow('frames',frame )
    if cv.waitKey(1)==27:
     break


cap.release()
cv.destroyAllWindows()
           
