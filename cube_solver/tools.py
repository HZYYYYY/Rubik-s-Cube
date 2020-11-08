import vision_params
import cv2
import os
import numpy as np
import kociemba
from collections import Counter
from recover import *
from rotate import *


def teach(problem,solution,step):
    step_now = solution.split(' ')[step]
    config = [problem[i*9: (i+1)*9] for i in range(6)]
    config = rotate(config, step_now)
    problem = ('').join(config)
    return problem



def del_duplicates(pts):
    """Delete one of two potential facelet centers stored in pts if they are too close to each other."""
    delta = width / 12  # width is defined global in grabcolors()
    dele = True
    while dele:
        dele = False
        r = range(len(pts))
        for i in r:
            for j in r[i + 1:]:
                if np.linalg.norm(pts[i] - pts[j]) < delta:
                    del pts[j]
                    dele = True
                if dele:
                    break
            if dele:
                break


def medoid(pts):
    """The mediod is the point with the smallest summed distance from the other points.
    This is a candidate for the center facelet."""
    res = np.array([0.0, 0.0])
    smin = 100000
    for i in pts:
        s = 0
        for j in pts:
            s += np.linalg.norm(i - j)
        if s < smin:
            smin = s
            res = i

    return res


def facelets(pts, med):
    """Separate the candidates into edge and corner facelets by their distance from the medoid."""
    ed = []
    co = []
    if med[0] == 0:
        return co, ed  # no edgefacelets detected
    # find shortest distance
    dmin = 10000
    for p in pts:
        d = np.linalg.norm(p - med)
        if 1 < d < dmin:
            dmin = d
    # edgefacelets should be in a distance not more than dmin*1.3
    for p in pts:
        d = np.linalg.norm(p - med)
        if dmin - 1 < d < dmin * 1.3:
            ed.append(p)
    # now find the corner facelets
    for p in pts:
        d = np.linalg.norm(p - med)
        if dmin * 1.3 < d < dmin * 1.7:
            co.append(p)
    return co, ed


def mirr_facelet(co, ed, med, width):
    """If we have detected a facelet position, the point reflection at the center also gives a facelet position.
     We can use this position in case the other facelet was not detected directly."""
    aef = []
    acf = []
    for p in ed:
        pa = 2 * med - p
        aef.append(pa)
    for p in co:
        pa = 2 * med - p
        acf.append(pa)

    # delete duplicates
    delta = width / 12  # width is defined global in grabcolors()
    #print(delta)
    for k in range(len(aef) - 1, -1, -1):
        for p in ed:
            if np.linalg.norm(aef[k] - p) < delta:
                del aef[k]
                break

    for k in range(len(acf) - 1, -1, -1):
        for p in co:
            if np.linalg.norm(acf[k] - p) < delta:
                del acf[k]
                break

    return acf, aef



def getcolor(p,hsv):
    """Decide the color of a facelet by its h value (non white) or by s and v (white)."""
    sz = 15
    p = p.astype(np.uint16)
    rect = hsv[p[1] - sz:p[1] + sz, p[0] - sz:p[0] + sz]
    median = np.sum(rect, axis=(0, 1)) / sz / sz / 4
    mh, ms, mv = median
    if ms <= vision_params.sat_W and mv >= vision_params.val_W:
        return median, 'white'
    elif vision_params.orange_L <= mh < vision_params.orange_H:
        return median, 'orange'
    elif vision_params.orange_H <= mh < vision_params.yellow_H:
        return median, 'yellow'
    elif vision_params.yellow_H <= mh < vision_params.green_H:
#         if ms < 150:
#             return median, 'white'  # green saturation is always higher
#         else:
        return median, 'green'
    elif vision_params.green_H <= mh < vision_params.blue_H:
        if ms < 150:
            return median, 'white'  # blue saturation is always higher
        else:
            return median, 'blue'
    else:
        return median, 'red'
    
def display_colorname(bgrcap, p,hsv):
    """Display the colornames on the webcam picture."""
    p = p.astype(np.uint16)
    med, col = getcolor(p,hsv)
    #final_col = col+' '+str(med[0])+' '+str(med[1])+' '+str(med[2])'
    if col in ('blue', 'green', 'red'):
        txtcol = (255, 255, 255)
    else:
        txtcol = (0, 0, 0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    tz = cv2.getTextSize(col, font, 0.4, 1)[0]
    #print('gdafgsrs')
    cv2.putText(
        bgrcap, col, tuple(p - (tz[0] // 2, -tz[1] // 2)), font, 0.4, txtcol, 1)
    #print('fdgfdg')

def getcolors(co, ed, aco, aed, m,hsv):
    """Find the colors of the 9 facelets and decide their position on the cube face."""
    centers = [[m for x in range(3)] for x in range(3)]
    colors = [['' for x in range(3)] for x in range(3)]
    s = np.array([0., 0., 0.])
    hsvs = [[s for x in range(3)] for x in range(3)]
    cocents = co + aco
    if len(cocents) == 0:
        return [], [],[]
    edcents = ed + aed
    if len(edcents) == 0:
        return [], [],[]
    for i in cocents:
        if i[0] < m[0] and i[1] < m[1]:
            centers[0][0] = i
        elif i[0] > m[0] and i[1] < m[1]:
            centers[0][2] = i
        elif i[0] < m[0] and i[1] > m[1]:
            centers[2][0] = i
        elif i[0] > m[0] and i[1] > m[1]:
            centers[2][2] = i
            
    if centers[0][0][0] == centers[1][1][0] and centers[0][0][1] == centers[1][1][1]:
        centers[0][0][0] = centers[1][1][0]+centers[0][2][1]-centers[1][1][1]
        centers[0][0][1] = centers[1][1][0]+centers[1][1][1]-centers[0][2][0]
        centers[2][2] = 2*centers[1][1]-centers[0][0]
        
    if centers[0][2][0] == centers[1][1][0] and centers[0][2][1] == centers[1][1][1]:
        centers[0][2][0] == centers[1][1][0]+centers[1][1][1]-centers[0][0][1]
        centers[0][2][1] == centers[0][0][0]+centers[1][1][1]-centers[1][1][0]
        centers[2][0] = 2*centers[1][1]-centers[0][2]

    centers[0][1] = (centers[0][0] +centers[0][2])/2
    centers[1][0] = (centers[0][0] +centers[2][0])/2
    centers[1][2] = (centers[0][2] +centers[2][2])/2
    centers[2][1] = (centers[2][0] +centers[2][2])/2
    
    color=str()
    for x in range(3):
        for y in range(3):
            hsv_, col = getcolor(centers[x][y],hsv)
            colors[x][y] = col
            if col=='red':
                color+='U'
            elif col=='white':
                color+='F'
            elif col=='green':
                color+='R'
            elif col=='blue':
                color+='L'
            elif col=='yellow':
                color+='B'
            elif col=='orange':
                color+='D'
            hsvs[x][y] = hsv_
    cents = []
    for i in range(3):
        for j in range(3):
            cents.append(centers[i][j])

    return hsvs, color,cents

def validate(cents, width):
    delta = width / 12  # width is defined global in grabcolors()
    dis = []
    dis.append(np.linalg.norm(cents[1]-cents[0]))
    dis.append(np.linalg.norm(cents[2]-cents[1]))
    dis.append(np.linalg.norm(cents[4]-cents[3]))
    dis.append(np.linalg.norm(cents[5]-cents[4]))
    dis.append(np.linalg.norm(cents[7]-cents[6]))
    dis.append(np.linalg.norm(cents[8]-cents[7]))
    
    dis.append(np.linalg.norm(cents[3]-cents[0]))
    dis.append(np.linalg.norm(cents[4]-cents[1]))
    dis.append(np.linalg.norm(cents[5]-cents[2]))
    dis.append(np.linalg.norm(cents[6]-cents[3]))
    dis.append(np.linalg.norm(cents[7]-cents[4]))
    dis.append(np.linalg.norm(cents[8]-cents[5]))
    
    edges_mean_sq = (np.sum(dis) / 12) ** 2
    edges_sq_mean = np.sum(np.square(dis)) / 12
#     if edges_sq_mean - edges_mean_sq>threshold:
#         return False
#     else:
#         return True
    return edges_sq_mean - edges_mean_sq 

def fit(cents):
    min_dis = np.inf
    for i in len(cents):
        for j in len(cents):
            if i < j and np.linalg.norm(cents[i]-cents[j])<min_dis :
                min_dis = np.linalg.norm(cents[i]-cents[j])
                facelet_1=cents[i]
                facelet_2=cents[j]
                

    

def solve(config):
    six_face=[]
    success=0
    solution=[]
    all_config = []
    for i in range(6):
        six_face.append(Counter(config[i]).most_common(1)[0][0])
    for i_1 in range(4):
        for i_2 in range(4):
            for i_3 in range(4):
                for i_4 in range(4):
                    for i_5 in range(4):
                        for i_6 in range(4):
                            problem=change(six_face[0],i_1)+change(six_face[1],i_2)+change(six_face[2],i_3)+change(six_face[3],i_4)+change(six_face[4],i_5)+change(six_face[5],i_6)
                            #print(problem)
                            try:
                                solution=kociemba.solve(problem)
                                all_config.append(problem)
                                #print('adfgfd')
                                success+=1
                            except:
                                pass
                            
    #problem=six_face[0]+six_face[1]+six_face[2]+six_face[3]+six_face[4]+six_face[5]
    try:
        solution=kociemba.solve(problem)
        success+=1
    except:
        pass
    return solution,success,all_config
    
def decide(action):
    if abs(action[1]) > abs(action[0]):
        if action[1] > 0:
            return 'Down'
        else:
            return 'Up'
    else:
        if action[0] > 0:
            return 'Left'
        else:
            return 'Right'     
        
def produce_can(problem):
    config_all = []
    for i in range(6):
        block = problem[i*9:(i+1)*9]
        for j in range(4):
            out = change(block, j)
            config_all.append(out)
    return config_all

def check(sub_problem, last_face, now_face, action):
    result = recover(sub_problem, last_face[4], now_face[4], action)
    if result[0] == last_face and result[1] == now_face:
        return True
    else:
        return False



def choose_from(relation):
    last_face = relation[0]
    now_face = relation[1]
    action = relation[2]
    problem = relation[3]
    new_problem = []
    for sub_problem in problem:
        if check(sub_problem, last_face, now_face, action):
            new_problem.append(sub_problem)
    return new_problem
    
def rectangle(center,edge,bgrcap):
    cv2.rectangle(bgrcap, (int(center[0]-edge),int(center[1]-edge)), (int(center[0]+edge),int(center[1]+edge)), (0, 0, 255), 3, 4, 0 )

def find_squares(bgrcap, n, color_mask, white_mask,hsv,height, width):
    """ Find the positions of squares in the webcam picture."""
    #global mask, color_mask, white_mask, black_mask,contours,final_contour,final_approx
    cent = []
    h, s, v = cv2.split(hsv)
    h_sqr = np.square(h)

    sz = height // n
    border = 1 * sz

    varmax_edges = 50

    # iterate all grid squares
    for y in range(border, height - border, sz):
        for x in range(border, width - border, sz):

            # compute the standard deviation sigma of the hue in the square
            rect_h = h[y:y + sz, x:x + sz]
            rect_h_sqr = h_sqr[y:y + sz, x:x + sz]
            median_h = np.sum(rect_h) / sz / sz
            sqr_median_h = median_h * median_h
            median_h_sqr = np.sum(rect_h_sqr) / sz / sz
            var = median_h_sqr - sqr_median_h
            sigma = np.sqrt(var)
            #print(sigma)

            delta = vision_params.delta_C

            # if sigma is small enough define a mask on the 3x3 square with the grid square in it's center
            if sigma < vision_params.sigma_W:
                rect3x3 = hsv[y - 1 * sz:y + 2 * sz, x - 1 * sz:x + 2 * sz]
                mask = cv2.inRange(rect3x3, (0, 0, vision_params.val_W),
                                   (255, vision_params.sat_W, 255))
            # and OR it to the white_mask
            white_mask[y - 1 * sz:y + 2 * sz, x - 1 * sz:x + 2 * sz] = \
                cv2.bitwise_or(mask, white_mask[y - 1 * sz:y + 2 * sz, x - 1 * sz:x + 2 * sz])

            # similar procedure for the color mask. Some issues because hues are computed modulo 180
            if sigma < vision_params.sigma_C:
                rect3x3 = h[y - 1 * sz:y + 2 * sz, x - 1 * sz:x + 2 * sz]
                if median_h + delta >= 180:
                   # print('aaaaaaa')
                    mask = cv2.inRange(rect3x3, 0, median_h + delta - 180)
                    mask = cv2.bitwise_or(mask, cv2.inRange(rect3x3, median_h - delta, 180))
                elif median_h - delta < 0:
                    #print('bbbbbb')
                    mask = cv2.inRange(rect3x3, median_h - delta + 180, 180)
                    mask = cv2.bitwise_or(mask, cv2.inRange(rect3x3, 0, median_h + delta))
                else:
                    mask = cv2.inRange(rect3x3, median_h - delta, median_h + delta)
                color_mask[y - 1 * sz:y + 2 * sz, x - 1 * sz:x + 2 * sz] = \
                    cv2.bitwise_or(mask, color_mask[y - 1 * sz:y + 2 * sz, x - 1 * sz:x + 2 * sz])

    black_mask = cv2.inRange(bgrcap, (0, 0, 0), (vision_params.rgb_L, vision_params.rgb_L, vision_params.rgb_L))
    black_mask = cv2.bitwise_not(black_mask)

    color_mask = cv2.bitwise_and(color_mask, black_mask)
    color_mask = cv2.blur(color_mask, (20, 20))
    color_mask = cv2.inRange(color_mask, 240, 255)

    white_mask = cv2.bitwise_and(white_mask, black_mask)
    white_mask = cv2.blur(white_mask, (20, 20))
    white_mask = cv2.inRange(white_mask, 240, 255)

    itr = iter([white_mask,color_mask])  # apply white filter first!
    final_contour = []
    final_approx = []

    # search for squares in the white_mask and in the color_mask
    for j in itr:        
        # find contours
        # works for OpenCV 3.2 or higher. For versions < 3.2 omit im2 in the line below.
        contours, hierarchy = cv2.findContours(j, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for n in range(len(contours)):
            approx = cv2.approxPolyDP(contours[n], sz // 2, True)
            # if the contour cannot be approximated by a quadrangle it is not a facelet square
            #print(approx.shape)
            if approx.shape[0] != 4:
                continue
            else:            
                final_contour.append(contours[n])
                
            corners = approx[:, 0]  # get the corners of the potential facelet square

            # the edges of the square should have all about the same length
            edges = np.array(
                [cv2.norm(corners[0] - corners[1], cv2.NORM_L2), cv2.norm(corners[1] - corners[2], cv2.NORM_L2),
                 cv2.norm(corners[2] - corners[3], cv2.NORM_L2),
                 cv2.norm(corners[3] - corners[0], cv2.NORM_L2)])
            edges_mean_sq = (np.sum(edges) / 4) ** 2
            edges_sq_mean = np.sum(np.square(edges)) / 4
            if edges_sq_mean - edges_mean_sq > varmax_edges:
                continue
            else:
                final_approx.append(approx)

            # cv2.drawContours(bgrcap, [approx], -1, (0, 0, 255), 8)
            middle = np.sum(corners, axis=0) / 4  # store the center of the potential facelet
            cent.append(np.asarray(middle))
    return cent

