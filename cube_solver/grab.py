import vision_params
import cv2
import os
import numpy as np
import kociemba
from draw import *
from rotate import *
from recover import *
from tools import *
from collections import Counter


def grab_colors():
    """Find the cube in the webcam picture and grab the colors of the facelets."""
    grid_N = 25  # number of grid-squares in vertical direction
    cap = cv2.VideoCapture(0)
    _, bgrcap = cap.read()
    old_bgrcap = bgrcap.copy()
    height, width = bgrcap.shape[:2]
    config_all = []
    detect = True
    last_relation = ''
    k = 0
    problem = []
    relation = None
    text2 = 0
    text3 = 0
    possibility = [0]
    
    optical_check = False
    last_face = '111111'
    move = []
    candidate = []
    
    start = (800,500)
    long = 30
    step = 0
    
    text="Rotate your cube"
    old_gray = cv2.cvtColor(bgrcap, cv2.COLOR_BGR2GRAY)
    
    for i in range(6):
        config_all.append([])
    while 1:

        # Take each frame
        facelet = []
        _, bgrcap = cap.read()  #
        
        new_frame = bgrcap.copy()
        gray_frame = cv2.cvtColor(bgrcap, cv2.COLOR_BGR2GRAY)

        # now set all hue values >160 to 0. This is important since the color red often contains hue values
        # in this range *and* also hue values >0 and else we get a mess when we compute mean and variance
        if detect ==True:
            hsv = cv2.cvtColor(bgrcap, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv)  #
            h_mask = cv2.inRange(h, 0, 160)
            h = cv2.bitwise_and(h, h, mask=h_mask)
            hsv = cv2.merge((h, s, v)).astype(float)

            # define two empty masks for the white-filter and the color-filter
            color_mask = cv2.inRange(bgrcap, np.array([1, 1, 1]), np.array([0, 0, 0]))  # mask for colors
            white_mask = cv2.inRange(bgrcap, np.array([1, 1, 1]), np.array([0, 0, 0]))  # special mask for white

            cent = []  # the centers of the facelet-square candidates are stored in this global variable
        
            draw_face(bgrcap, config_all,start,long)
            
            cent = find_squares(bgrcap, grid_N, color_mask, white_mask, hsv,height, width)  # find the candida
            
            m = medoid(cent)
            cf, ef = facelets(cent, m)  # identify the centers of the corner and edge facelets

            acf, aef = mirr_facelet(cf, ef, m,width)

            vision_params.face_hsv, vision_params.face_col,cents = getcolors(cf, ef, acf, aef, m, hsv)
            if len(cents)>4 and validate(cents,width)<10:
                for i in cents:
                    display_colorname(bgrcap, i,hsv)
                if optical_check:
                    center = cents[4]
                    edge = np.linalg.norm(cents[5] - cents[4])
                    if vision_params.face_col[4] != last_face[4] and vision_params.face_col in candidate:
                        if len(move)>0:
                            motion = np.mean(move,axis=0)
                            if abs(motion[0] - motion[1]) >= 1:
                                action = decide(motion)
                                text = action + str(motion)
                                relation = (last_face, vision_params.face_col, action, problem)

                        last_face = vision_params.face_col
                        move = []
                        config_all = []
                        for i in range(6):
                            config_all.append([])
                        
                    if text2 != 0:
                        cv2.putText(bgrcap, text2, (100, 150), cv2.FONT_HERSHEY_PLAIN, 4.0, (0, 0, 255), 2)
                    if text3 != 0:
                        cv2.putText(bgrcap, text3, (100, 250), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 255), 1)
                    try:
                        pred_labels = nn.predict_from_img_pairs([[old_bgrcap[int(center[0]-edge):int(center[0]+edge), int(center[1]-edge):int(center[1]+edge),:],new_frame[int(center[0]-edge):int(center[0]+edge), int(center[1]-edge):int(center[1]+edge),:]]], batch_size=1, verbose=False)
                        flow = pred_labels[0]
                        move.append([np.mean(flow[:,:,0]),np.mean(flow[:,:,1])])
                        optical_frame = flow_to_img(pred_labels[0])
                        old_bgrcap = new_frame.copy()
                        rectangle(center,edge,bgrcap)
                        cv2.imshow("optical_frame",optical_frame)
                    except:
                        pass

                    if (relation is not None) and relation != last_relation:
                        temp = problem 
                        problem = choose_from(relation)
                        last_relation = relation
                        if len(problem) != 0:
                            for i in problem:
                                possibility[temp.index(i)] += 1

                        problem = temp
                        text2 = str(len(problem))+' ' +'candidate solutions'
                        text3 = str(possibility)

                else:
                    if vision_params.face_col[4] == 'U':
                        config_all[0].append(vision_params.face_col)
                    if vision_params.face_col[4] == 'R':
                        config_all[1].append(vision_params.face_col)
                    if vision_params.face_col[4] == 'F':
                        config_all[2].append(vision_params.face_col)
                    if vision_params.face_col[4] == 'D':
                        config_all[3].append(vision_params.face_col)
                    if vision_params.face_col[4] == 'L':
                        config_all[4].append(vision_params.face_col)
                    if vision_params.face_col[4] == 'B':
                        config_all[5].append(vision_params.face_col)
            
        else:
            draw(bgrcap,problem,start,long)
            draw_sol(bgrcap,start,long,solution,step)
                
            # 'n'
            if k == 110:  
                problem = teach(problem, solution,step)
                step += 1
                if step == len(solution.split(' ')):
                    text = " Solved!!!"
                    detect = True
                    cv2.destroyAllWindows()
                    break
                    

        cv2.putText(bgrcap, text, (100, 50), cv2.FONT_HERSHEY_PLAIN, 4.0, (0, 0, 255), 2)
        
        
        cv2.imshow('Webcam - type "x" to quit.', bgrcap)
        
        flag = True
        for i in range(6):
            if len(config_all[i]) == 0:
                flag = False
                
        if sum(possibility) !=  0:
            sorted_pos = sorted(possibility)
            if sorted_pos[-1] - sorted_pos[-2] >= 3:
                pro_index = possibility.index(max(possibility))
                solution = kociemba.solve(problem[pro_index])
                text = "Solution found!"

                config_all = []
                for i in range(6):
                    config_all.append([])
                print('finished')
                print(solution)
                problem = problem[pro_index]
                possibility = [0]
                detect = False
            
        if flag:   
            solution,success,problem = solve(config_all)
            problem = list(set(problem))
            possibility = [0 for i in range(len(problem))]
            if success>1:
                text = "Candidate Solution found!"
                text2 = str(len(problem))+' ' +'candidate solutions'
                candidate = produce_can(problem[-1])
                optical_check = True
                config_all = []
                for i in range(6):
                    config_all.append([])

            elif success>0:
                problem = problem[0]
                text = "Solution found!"
                config_all = []
                for i in range(6):
                    config_all.append([])
                print('finished')
                print(solution)
                detect = False
                
            
        
        k = cv2.waitKey(5) & 0xFF
        if k == 120:  # type x to exit
            cv2.destroyAllWindows()
            break