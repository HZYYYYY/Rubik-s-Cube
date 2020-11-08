import cv2
import os
import numpy as np
from collections import Counter

def draw_sol (img,start,long,solution,step):
    step_now = solution.split(' ')[step]
    if step_now[0] == 'U':
        start_now = (start[0] + 3*long,start[1] - 3*long )
    if step_now[0] == 'F':
        start_now = (start[0] + 3*long,start[1] )
    if step_now[0] == 'L':
        start_now = start
    if step_now[0] == 'R':
        start_now = (start[0] + 6*long,start[1]  )
    if step_now[0] == 'B':
        start_now = (start[0] + 9*long,start[1]  )
    if step_now[0] == 'D':
        start_now = (start[0] + 3*long,start[1] + 3*long )
    
    if len(step_now) == 1:
        cv2.arrowedLine(img, start_now,(start_now[0]+3*long,start_now[1]), (0,0,255), 5)   
    elif step_now[1] == "'":        
        cv2.arrowedLine(img,(start_now[0]+3*long,start_now[1]),start_now, (0,0,255), 5)     
    elif step_now[1] == "2":
        cv2.arrowedLine(img, start_now,(start_now[0]+3*long,start_now[1]), (0,0,0), 5)     
    
    cv2.rectangle(img, start_now, (start_now[0]+3*long,start_now[1]+3*long), (0, 0, 255), 3) 

def draw(img,problem,start, long):
    for i in range(6):
        sub_p = problem[i*9:(i+1)*9]
        sub_draw(img, i , sub_p,start,long)
        
def sub_draw(img, i , sub_p,start,long):
    if i==0:
        sub_start = (start[0] + long*3 ,start[1]-long*3)
    if i==1:
        sub_start = (start[0] + long*6 ,start[1])
    if i==2:
        sub_start = (start[0] + long*3 ,start[1])
    if i==3:
        sub_start = (start[0] + long*3 ,start[1]+long*3)
    if i==4:
        sub_start = (start[0]  ,start[1])
    if i==5:
        sub_start = (start[0] + long*9  ,start[1])
    
    for j in range(len(sub_p)):
        sub_draw_1(img,sub_start,j, sub_p[j],long)
        
def  sub_draw_1(img,sub_start, j, signal,long):
    if signal == 'U':
        color = (0,0,255)
    if signal == 'F':
        color = (255,255,255)
    if signal== 'R':
        color = (0,255,0)
    if signal== 'L':
        color = (255,0,0)
    if signal == 'D':
        color = (0, 165, 255)
    if signal == 'B':
        color = (0,255,255)
    #cv2.rectangle(img, (800, 500), (830, 530), (0, 0, 0), -1)
    #print((sub_start[0]+(j%3)*long, sub_start[0]+(j//3)*long), (sub_start[0]+(j%3 + 1)*long, sub_start[0]+(j//3 + 1)*long), color)
    cv2.rectangle(img, (sub_start[0]+(j%3)*long, sub_start[1]+(j//3)*long), (sub_start[0]+(j%3 + 1)*long, sub_start[1]+(j//3 + 1)*long), color, -1) 

def drawgrid(img, n):
    """Draw grid onto the webcam output. Only used for debugging purposes."""
    h, w = img.shape[:2]
    sz = h // n
    border = 1 * sz
    for y in range(border, h - border, sz):
        for x in range(border, w - border, sz):
            cv2.rectangle(img, (x, y), (x + sz, y + sz), (0, 0, 0), 1)  # plot small squares in black and white
            cv2.rectangle(img, (x - 1, y - 1), (x + 1 + sz, y + 1 + sz), (255, 255, 255), 1)

def draw_face(img, config_all,start,long):
    for i in range(6):
        if len(config_all[i]) != 0:
            face = Counter(config_all[i]).most_common(1)[0][0]
            sub_draw(img, i , face,start,long)