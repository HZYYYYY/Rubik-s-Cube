def recover(sub_problem, face_1, face_2, action):
    config = []
    for i in range(6):
        config.append(sub_problem[i*9:(i+1)*9])
    if face_1 == "F":
        if face_2 == "U":
            if action == "Up":
                return [change(config[2], 1), change(config[0], 1)]
            if action == "Down":
                return [change(config[2], 0), change(config[0], 0)]
            if action == "Left":
                return [change(config[2], 2), change(config[0], 2)]
            if action == "Right":
                return [change(config[2], 3), change(config[0], 3)]
        if face_2 == "R":
            if action == "Up":
                return [change(config[2], 3), change(config[1], 3)]
            if action == "Down":
                return [change(config[2], 2), change(config[1], 2)]
            if action == "Left":
                return [change(config[2], 1), change(config[1], 1)]
            if action == "Right":
                return [change(config[2], 0), change(config[1], 0)]
        if face_2 == "L":
            if action == "Up":
                return [change(config[2], 2), change(config[4], 2)]
            if action == "Down":
                return [change(config[2], 3), change(config[4], 3)]
            if action == "Left":
                return [change(config[2], 0), change(config[4], 0)]
            if action == "Right":
                return [change(config[2], 1), change(config[4], 1)]
        if face_2 == "D":
            if action == "Up":
                return [change(config[2], 0), change(config[3], 0)]
            if action == "Down":
                return [change(config[2], 1), change(config[3], 1)]
            if action == "Left":
                return [change(config[2], 3), change(config[3], 3)]
            if action == "Right":
                return [change(config[2], 2), change(config[3], 2)]
            
    if face_1 == "U":
        if face_2 == "B":
            if action == "Up":
                return [change(config[0], 1), change(config[5], 0)]
            if action == "Down":
                return [change(config[0], 0), change(config[5], 1)]
            if action == "Left":
                return [change(config[0], 2), change(config[5], 3)]
            if action == "Right":
                return [change(config[0], 3), change(config[5], 2)]
        if face_2 == "F":
            if action == "Up":
                return [change(config[0], 0), change(config[2], 0)]
            if action == "Down":
                return [change(config[0], 1), change(config[2], 1)]
            if action == "Left":
                return [change(config[0], 3), change(config[2], 3)]
            if action == "Right":
                return [change(config[0], 2), change(config[2], 2)]
        if face_2 == "L":
            if action == "Up":
                return [change(config[0], 2), change(config[4], 0)]
            if action == "Down":
                return [change(config[0], 3), change(config[4], 1)]
            if action == "Left":
                return [change(config[0], 0), change(config[4], 3)]
            if action == "Right":
                return [change(config[0], 1), change(config[4], 2)]
        if face_2 == "R":
            if action == "Up":
                return [change(config[0], 3), change(config[1], 0)]
            if action == "Down":
                return [change(config[0], 2), change(config[1], 1)]
            if action == "Left":
                return [change(config[0], 1), change(config[1], 3)]
            if action == "Right":
                return [change(config[0], 0), change(config[1], 2)]
            
    if face_1 == "R":
        if face_2 == "U":
            if action == "Up":
                return [change(config[1], 1), change(config[0], 2)]
            if action == "Down":
                return [change(config[1], 0), change(config[0], 3)]
            if action == "Left":
                return [change(config[1], 2), change(config[0], 0)]
            if action == "Right":
                return [change(config[1], 3), change(config[0], 1)]
        if face_2 == "F":
            if action == "Up":
                return [change(config[1], 2), change(config[2], 2)]
            if action == "Down":
                return [change(config[1], 3), change(config[2], 3)]
            if action == "Left":
                return [change(config[1], 0), change(config[2], 0)]
            if action == "Right":
                return [change(config[1], 1), change(config[2], 1)]
        if face_2 == "B":
            if action == "Up":
                return [change(config[1], 3), change(config[5], 3)]
            if action == "Down":
                return [change(config[1], 2), change(config[5], 2)]
            if action == "Left":
                return [change(config[1], 1), change(config[5], 1)]
            if action == "Right":
                return [change(config[1], 0), change(config[5], 0)]
        if face_2 == "D":
            if action == "Up":
                return [change(config[1], 0), change(config[3], 2)]
            if action == "Down":
                return [change(config[1], 1), change(config[3], 3)]
            if action == "Left":
                return [change(config[1], 3), change(config[3], 0)]
            if action == "Right":
                return [change(config[1], 2), change(config[3], 1)]
            
    if face_1 == "D":
        if face_2 == "R":
            if action == "Up":
                return [change(config[3], 3), change(config[1], 1)]
            if action == "Down":
                return [change(config[3], 2), change(config[1], 0)]
            if action == "Left":
                return [change(config[3], 1), change(config[1], 2)]
            if action == "Right":
                return [change(config[3], 0), change(config[1], 3)]
        if face_2 == "F":
            if action == "Up":
                return [change(config[3], 1), change(config[2], 1)]
            if action == "Down":
                return [change(config[3], 0), change(config[2], 0)]
            if action == "Left":
                return [change(config[3], 2), change(config[2], 2)]
            if action == "Right":
                return [change(config[3], 3), change(config[2], 3)]
        if face_2 == "B":
            if action == "Up":
                return [change(config[3], 0), change(config[5], 1)]
            if action == "Down":
                return [change(config[3], 1), change(config[5], 0)]
            if action == "Left":
                return [change(config[3], 3), change(config[5], 2)]
            if action == "Right":
                return [change(config[3], 2), change(config[5], 3)]
        if face_2 == "L":
            if action == "Up":
                return [change(config[3], 2), change(config[4], 1)]
            if action == "Down":
                return [change(config[3], 3), change(config[4], 0)]
            if action == "Left":
                return [change(config[3], 0), change(config[4], 2)]
            if action == "Right":
                return [change(config[3], 1), change(config[4], 3)]
            
    if face_1 == "L":
        if face_2 == "U":
            if action == "Up":
                return [change(config[4], 1), change(config[0], 3)]
            if action == "Down":
                return [change(config[4], 0), change(config[0], 2)]
            if action == "Left":
                return [change(config[4], 2), change(config[0], 1)]
            if action == "Right":
                return [change(config[4], 3), change(config[0], 0)]
        if face_2 == "F":
            if action == "Up":
                return [change(config[4], 3), change(config[2], 3)]
            if action == "Down":
                return [change(config[4], 2), change(config[2], 2)]
            if action == "Left":
                return [change(config[4], 1), change(config[2], 1)]
            if action == "Right":
                return [change(config[4], 0), change(config[2], 0)]
        if face_2 == "B":
            if action == "Up":
                return [change(config[4], 2), change(config[5], 2)]
            if action == "Down":
                return [change(config[4], 3), change(config[5], 3)]
            if action == "Left":
                return [change(config[4], 0), change(config[5], 0)]
            if action == "Right":
                return [change(config[4], 1), change(config[5], 1)]
        if face_2 == "D":
            if action == "Up":
                return [change(config[4], 0), change(config[3], 3)]
            if action == "Down":
                return [change(config[4], 1), change(config[3], 2)]
            if action == "Left":
                return [change(config[4], 3), change(config[3], 1)]
            if action == "Right":
                return [change(config[4], 2), change(config[3], 0)]
            
    if face_1 == "B":
        if face_2 == "U":
            if action == "Up":
                return [change(config[5], 1), change(config[0], 0)]
            if action == "Down":
                return [change(config[5], 0), change(config[0], 1)]
            if action == "Left":
                return [change(config[5], 2), change(config[0], 3)]
            if action == "Right":
                return [change(config[5], 3), change(config[0], 2)]
        if face_2 == "L":
            if action == "Up":
                return [change(config[5], 3), change(config[4], 3)]
            if action == "Down":
                return [change(config[5], 2), change(config[4], 2)]
            if action == "Left":
                return [change(config[5], 1), change(config[4], 1)]
            if action == "Right":
                return [change(config[5], 0), change(config[4], 0)]
        if face_2 == "R":
            if action == "Up":
                return [change(config[5], 2), change(config[1], 2)]
            if action == "Down":
                return [change(config[5], 3), change(config[1], 3)]
            if action == "Left":
                return [change(config[5], 0), change(config[1], 0)]
            if action == "Right":
                return [change(config[5], 1), change(config[1], 1)]
        if face_2 == "D":
            if action == "Up":
                return [change(config[5], 0), change(config[3], 1)]
            if action == "Down":
                return [change(config[5], 1), change(config[3], 0)]
            if action == "Left":
                return [change(config[5], 3), change(config[3], 2)]
            if action == "Right":
                return [change(config[5], 2), change(config[3], 3)]

    
def rotate(config, direction):
    # U--0
    new_fig = []
    for i in range(6):
        new_fig.append([])
    if direction == "U":
        new_fig[0] = config[0][6]+config[0][3]+config[0][0]+config[0][7]+config[0][4]+config[0][1]+config[0][8]+config[0][5]+config[0][2]
        new_fig[1] = config[5][:3] +config[1][3:]
        new_fig[2] = config[1][:3] +config[2][3:]
        new_fig[3] = config[3]
        new_fig[4] = config[2][:3] +config[4][3:]
        new_fig[5] = config[4][:3] +config[5][3:]
    if direction == "U2":
        new_fig[0] = config[0][8]+config[0][7]+config[0][6]+config[0][5]+config[0][4]+config[0][3]+config[0][2]+config[0][1]+config[0][0]
        new_fig[1] = config[4][:3] +config[1][3:]
        new_fig[2] = config[5][:3] +config[2][3:]
        new_fig[3] = config[3]
        new_fig[4] = config[1][:3] +config[4][3:]
        new_fig[5] = config[2][:3] +config[5][3:]
    if direction == "U'":
        new_fig[0] = config[0][2]+config[0][5]+config[0][8]+config[0][1]+config[0][4]+config[0][7]+config[0][0]+config[0][3]+config[0][6]
        new_fig[1] = config[2][:3] +config[1][3:]
        new_fig[2] = config[4][:3] +config[2][3:]
        new_fig[3] = config[3]
        new_fig[4] = config[5][:3] +config[4][3:]
        new_fig[5] = config[1][:3] +config[5][3:]
    # R--1
    if direction == "R":      
        new_fig[1] = config[1][6]+config[1][3]+config[1][0]+config[1][7]+config[1][4]+config[1][1]+config[1][8]+config[1][5]+config[1][2]
        new_fig[0] = config[0][0]+config[0][1]+config[2][2]+config[0][3]+config[0][4]+config[2][5]+config[0][6]+config[0][7]+config[2][8]
        new_fig[2] = config[2][0]+config[2][1]+config[3][2]+config[2][3]+config[2][4]+config[3][5]+config[2][6]+config[2][7]+config[3][8]
        new_fig[3] = config[3][0]+config[3][1]+config[5][6]+config[3][3]+config[3][4]+config[5][3]+config[3][6]+config[3][7]+config[5][0]
        new_fig[4] = config[4]
        new_fig[5] = config[0][8]+config[5][1]+config[5][2]+config[0][5]+config[5][4]+config[5][5]+config[0][2]+config[5][7]+config[5][8]
    if direction == "R2":
        new_fig[1] = config[1][8]+config[1][7]+config[1][6]+config[1][5]+config[1][4]+config[1][3]+config[1][2]+config[1][1]+config[1][0]
        new_fig[0] = config[0][0]+config[0][1]+config[3][2]+config[0][3]+config[0][4]+config[3][5]+config[0][6]+config[0][7]+config[3][8]
        new_fig[2] = config[2][0]+config[2][1]+config[5][6]+config[2][3]+config[2][4]+config[5][3]+config[2][6]+config[2][7]+config[5][0]
        new_fig[3] = config[3][0]+config[3][1]+config[0][2]+config[3][3]+config[3][4]+config[0][5]+config[3][6]+config[3][7]+config[0][8]
        new_fig[4] = config[4]
        new_fig[5] = config[2][8]+config[5][1]+config[5][2]+config[2][5]+config[5][4]+config[5][5]+config[2][2]+config[5][7]+config[5][8]
    if direction == "R'":
        new_fig[1] = config[1][2]+config[1][5]+config[1][8]+config[1][1]+config[1][4]+config[1][7]+config[1][0]+config[1][3]+config[1][6]
        new_fig[0] = config[0][0]+config[0][1]+config[5][6]+config[0][3]+config[0][4]+config[5][3]+config[0][6]+config[0][7]+config[5][0]
        new_fig[2] = config[2][0]+config[2][1]+config[0][2]+config[2][3]+config[2][4]+config[0][5]+config[2][6]+config[2][7]+config[0][8]
        new_fig[3] = config[3][0]+config[3][1]+config[2][2]+config[3][3]+config[3][4]+config[2][5]+config[3][6]+config[3][7]+config[2][8]
        new_fig[4] = config[4]
        new_fig[5] = config[3][8]+config[5][1]+config[5][2]+config[3][5]+config[5][4]+config[5][5]+config[3][2]+config[5][7]+config[5][8]
    
    # F--2
    if direction == "F":
        new_fig[2] = config[2][6]+config[2][3]+config[2][0]+config[2][7]+config[2][4]+config[2][1]+config[2][8]+config[2][5]+config[2][2]
        new_fig[0] = config[0][:6]+ config[4][8] +config[4][5]+config[4][2]
        new_fig[1] = config[0][6]+config[1][1]+config[1][2]+config[0][7]+config[1][4]+config[1][5]+config[0][8]+config[1][7]+config[1][8]
        new_fig[3] = config[1][6]+config[1][3]+config[1][0]+config[3][3:]
        new_fig[4] = config[4][0]+config[4][1]+config[3][0]+config[4][3]+config[4][4]+config[3][1]+config[4][6]+config[4][7]+config[3][2]  
        new_fig[5] = config[5]
    if direction == "F2":
        new_fig[2] = config[2][8]+config[2][7]+config[2][6]+config[2][5]+config[2][4]+config[2][3]+config[2][2]+config[2][1]+config[2][0]
        new_fig[0] = config[0][:6]+ config[3][2] +config[3][1]+config[3][0]
        new_fig[1] = config[4][8]+config[1][1]+config[1][2]+config[4][5]+config[1][4]+config[1][5]+config[4][2]+config[1][7]+config[1][8]
        new_fig[3] = config[0][8]+config[0][7]+config[0][6]+config[3][3:]
        new_fig[4] = config[4][0]+config[4][1]+config[1][6]+config[4][3]+config[4][4]+config[1][3]+config[4][6]+config[4][7]+config[1][0]  
        new_fig[5] = config[5]
        
    if direction == "F'":
        new_fig[2] = config[2][2]+config[2][5]+config[2][8]+config[2][1]+config[2][4]+config[2][7]+config[2][0]+config[2][3]+config[2][6]  
        new_fig[0] = config[0][:6]+ config[1][0] +config[1][3]+config[1][6]
        new_fig[1] = config[3][2]+config[1][1]+config[1][2]+config[3][1]+config[1][4]+config[1][5]+config[3][0]+config[1][7]+config[1][8]
        new_fig[3] = config[4][2]+config[4][5]+config[4][8]+config[3][3:]
        new_fig[4] = config[4][0]+config[4][1]+config[0][8]+config[4][3]+config[4][4]+config[0][7]+config[4][6]+config[4][7]+config[0][6]
        new_fig[5] = config[5]
   
    # D--3  
    if direction == "D":
        new_fig[3] = config[3][6]+config[3][3]+config[3][0]+config[3][7]+config[3][4]+config[3][1]+config[3][8]+config[3][5]+config[3][2]
        new_fig[0] = config[0]
        new_fig[1] = config[1][:6] +config[2][6:]
        new_fig[2] = config[2][:6] +config[4][6:]
        new_fig[4] = config[4][:6] +config[5][6:]
        new_fig[5] = config[5][:6] +config[1][6:]
    if direction == "D2":
        new_fig[3] = config[3][8]+config[3][7]+config[3][6]+config[3][5]+config[3][4]+config[3][3]+config[3][2]+config[3][1]+config[3][0]
        new_fig[0] = config[0]
        new_fig[1] = config[1][:6] +config[4][6:]
        new_fig[2] = config[2][:6] +config[5][6:]
        new_fig[4] = config[4][:6] +config[1][6:]
        new_fig[5] = config[5][:6] +config[2][6:]
    if direction == "D'":
        new_fig[3] = config[3][2]+config[3][5]+config[3][8]+config[3][1]+config[3][4]+config[3][7]+config[3][0]+config[3][3]+config[3][6]  
        new_fig[0] = config[0]
        new_fig[1] = config[1][:6] +config[5][6:]
        new_fig[2] = config[2][:6] +config[1][6:]
        new_fig[4] = config[4][:6] +config[2][6:]
        new_fig[5] = config[5][:6] +config[4][6:]
     
    # L--4
    if direction == "L":
        new_fig[4] = config[4][6]+config[4][3]+config[4][0]+config[4][7]+config[4][4]+config[4][1]+config[4][8]+config[4][5]+config[4][2]
        new_fig[0] = config[5][8]+config[0][1]+config[0][2]+config[5][5]+config[0][4]+config[0][5]+config[5][2]+config[0][7]+config[0][8]
        new_fig[1] = config[1]
        new_fig[2] = config[0][0]+config[2][1]+config[2][2]+config[0][3]+config[2][4]+config[2][5]+config[0][6]+config[2][7]+config[2][8]
        new_fig[3] = config[2][0]+config[3][1]+config[3][2]+config[2][3]+config[3][4]+config[3][5]+config[2][6]+config[3][7]+config[3][8]
        new_fig[5] = config[5][0]+config[5][1]+config[3][6]+config[5][3]+config[5][4]+config[3][3]+config[5][6]+config[5][7]+config[3][0]
    if direction == "L2":
        new_fig[4] = config[4][8]+config[4][7]+config[4][6]+config[4][5]+config[4][4]+config[4][3]+config[4][2]+config[4][1]+config[4][0]
        new_fig[0] = config[3][0]+config[0][1]+config[0][2]+config[3][3]+config[0][4]+config[0][5]+config[3][6]+config[0][7]+config[0][8]
        new_fig[1] = config[1]
        new_fig[2] = config[5][8]+config[2][1]+config[2][2]+config[5][5]+config[2][4]+config[2][5]+config[5][2]+config[2][7]+config[2][8]
        new_fig[3] = config[0][0]+config[3][1]+config[3][2]+config[0][3]+config[3][4]+config[3][5]+config[0][6]+config[3][7]+config[3][8]
        new_fig[5] = config[5][0]+config[5][1]+config[2][6]+config[5][3]+config[5][4]+config[2][3]+config[5][6]+config[5][7]+config[2][0]
    if direction == "L'":
        new_fig[4] = config[4][2]+config[4][5]+config[4][8]+config[4][1]+config[4][4]+config[4][7]+config[4][0]+config[4][3]+config[4][6] 
        new_fig[0] = config[2][0]+config[0][1]+config[0][2]+config[2][3]+config[0][4]+config[0][5]+config[2][6]+config[0][7]+config[0][8]
        new_fig[1] = config[1]
        new_fig[2] = config[3][0]+config[2][1]+config[2][2]+config[3][3]+config[2][4]+config[2][5]+config[3][6]+config[2][7]+config[2][8]
        new_fig[3] = config[5][8]+config[3][1]+config[3][2]+config[5][5]+config[3][4]+config[3][5]+config[5][2]+config[3][7]+config[3][8]
        new_fig[5] = config[5][0]+config[5][1]+config[0][6]+config[5][3]+config[5][4]+config[0][3]+config[5][6]+config[5][7]+config[0][0]
    
    # B--5
    if direction == "B":
        new_fig[5] = config[5][6]+config[5][3]+config[5][0]+config[5][7]+config[5][4]+config[5][1]+config[5][8]+config[5][5]+config[5][2]
        new_fig[0] = config[1][2] + config[1][5] + config[1][8] + config[0][3:]
        new_fig[1] = config[1][0]+config[1][1]+config[3][8]+config[1][3]+config[1][4]+config[3][7]+config[1][6]+config[1][7]+config[3][6]
        new_fig[2] = config[2]
        new_fig[3] = config[3][:6]+config[4][0]+config[4][3]+config[4][6]
        new_fig[4] = config[0][2]+config[4][1]+config[4][2]+config[0][1]+config[4][4]+config[4][5]+config[0][0]+config[4][7]+config[4][8] 
        
    if direction == "B2":
        new_fig[5] = config[5][8]+config[5][7]+config[5][6]+config[5][5]+config[5][4]+config[5][3]+config[5][2]+config[5][1]+config[5][0]
        new_fig[0] = config[3][8] + config[3][7] + config[3][6] + config[0][3:]
        new_fig[1] = config[1][0]+config[1][1]+config[4][6]+config[1][3]+config[1][4]+config[4][3]+config[1][6]+config[1][7]+config[4][0]
        new_fig[2] = config[2]
        new_fig[3] = config[3][:6]+config[0][2]+config[0][1]+config[0][0]
        new_fig[4] = config[1][8]+config[4][1]+config[4][2]+config[1][5]+config[4][4]+config[4][5]+config[1][2]+config[4][7]+config[4][8] 
    if direction == "B'":
        new_fig[5] = config[5][2]+config[5][5]+config[5][8]+config[5][1]+config[5][4]+config[5][7]+config[5][0]+config[5][3]+config[5][6]  
        new_fig[0] = config[4][6] + config[4][3] + config[4][0] + config[0][3:]
        new_fig[1] = config[1][0]+config[1][1]+config[0][0]+config[1][3]+config[1][4]+config[0][1]+config[1][6]+config[1][7]+config[0][2]
        new_fig[2] = config[2]
        new_fig[3] = config[3][:6]+config[1][8]+config[1][5]+config[1][2]
        new_fig[4] = config[3][6]+config[4][1]+config[4][2]+config[3][7]+config[4][4]+config[4][5]+config[3][8]+config[4][7]+config[4][8] 
    return new_fig

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

        
def teach(problem,solution,step):
    step_now = solution.split(' ')[step]
    config = [problem[i*9: (i+1)*9] for i in range(6)]
    config = rotate(config, step_now)
    problem = ('').join(config)
    return problem
    
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

import vision_params
import cv2
import os
import numpy as np
import kociemba
from collections import Counter

grid_N = 25  # number of grid-squares in vertical direction


def drawgrid(img, n):
    """Draw grid onto the webcam output. Only used for debugging purposes."""
    h, w = img.shape[:2]
    sz = h // n
    border = 1 * sz
    for y in range(border, h - border, sz):
        for x in range(border, w - border, sz):
            cv2.rectangle(img, (x, y), (x + sz, y + sz), (0, 0, 0), 1)  # plot small squares in black and white
            cv2.rectangle(img, (x - 1, y - 1), (x + 1 + sz, y + 1 + sz), (255, 255, 255), 1)


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


def mirr_facelet(co, ed, med):
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



def getcolor(p):
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
    
def display_colorname(bgrcap, p):
    """Display the colornames on the webcam picture."""
    p = p.astype(np.uint16)
    med, col = getcolor(p)
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


def getcolors(co, ed, aco, aed, m):
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
            hsv_, col = getcolor(centers[x][y])
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




def find_squares(bgrcap, n):
    """ Find the positions of squares in the webcam picture."""
    global mask, color_mask, white_mask, black_mask,contours,final_contour,final_approx

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
    
#     kernel = np.ones((5,5),np.uint8)  
#     color_mask = cv2.erode(color_mask,kernel,iterations = 5)

    itr = iter([white_mask,color_mask])  # apply white filter first!
    final_contour = []
    final_approx = []

    # search for squares in the white_mask and in the color_mask
    for j in itr:        
        # print(j,"okokokok")
        # find contours
        # works for OpenCV 3.2 or higher. For versions < 3.2 omit im2 in the line below.
        contours, hierarchy = cv2.findContours(j, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #print(contours[1].shape,'adfds')
        
        #print(len(contours))
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
            #print(edges_sq_mean - edges_mean_sq,'haha')
            if edges_sq_mean - edges_mean_sq > varmax_edges:
                continue
            else:
                final_approx.append(approx)

            # cv2.drawContours(bgrcap, [approx], -1, (0, 0, 255), 8)
            middle = np.sum(corners, axis=0) / 4  # store the center of the potential facelet
            cent.append(np.asarray(middle))
            

def validate(cents):
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
                
def change(face,index):
    if index==0:
        output = face
    if index==1:
        output = face[::-1]
    if index==2:
        output = face[2]+face[5]+face[8]+face[1]+face[4]+face[7]+face[0]+face[3]+face[6]
    if index==3:
        output = face[6]+face[3]+face[0]+face[7]+face[4]+face[1]+face[8]+face[5]+face[2]
    return output
    
# def solve(config):
#     six_face=[]
#     success=0
#     solution=[]
#     for i in range(6):
#         six_face.append(Counter(config[i]).most_common(1)[0][0])
                            
#     problem=six_face[0]+six_face[1]+six_face[2]+six_face[3]+six_face[4]+six_face[5]
#     try:
#         solution=kociemba.solve(problem)
#         success+=1
#     except:
#         pass
#     return solution,success,problem

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
    


def grab_colors():
    """Find the cube in the webcam picture and grab the colors of the facelets."""
    global cent, width, height, hsv, color_mask, white_mask,contours,final_contour,final_approx
    cap = cv2.VideoCapture(0)
    _, bgrcap = cap.read()
    #bgrcap =  cv2.imread('three_face.jpg')
    height, width = bgrcap.shape[:2]
    config_all = []
    finish = False # decide whether finish
    solutions = []
    detect = True
    last_problem = ''
    k = 0
    problem = []
    relation = None
    
    point_selected = False
    last_face = '111111'
    move = []
    candidate = []
    
    start = (800,500)
    long = 30
    step = 0
    
    text="Rotate your cube"
    old_gray = cv2.cvtColor(bgrcap, cv2.COLOR_BGR2GRAY)
    # Lucas kanade params
    lk_params = dict(winSize = (15, 15),
                     maxLevel = 4,
                     criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    
    for i in range(6):
        config_all.append([])
    while 1:

        # Take each frame
        facelet = []
    
        _, bgrcap = cap.read()  #
        bgrcap = cv2.blur(bgrcap, (5, 5))
        gray_frame = cv2.cvtColor(bgrcap, cv2.COLOR_BGR2GRAY)

        # now set all hue values >160 to 0. This is important since the color red often contains hue values
        # in this range *and* also hue values >0 and else we get a mess when we compute mean and variance
        hsv = cv2.cvtColor(bgrcap, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)  #
        #print(len(h[h>200]),'hasfjkhadsf')
        h_mask = cv2.inRange(h, 0, 160)
        h = cv2.bitwise_and(h, h, mask=h_mask)
        hsv = cv2.merge((h, s, v)).astype(float)

        # define two empty masks for the white-filter and the color-filter
        color_mask = cv2.inRange(bgrcap, np.array([1, 1, 1]), np.array([0, 0, 0]))  # mask for colors
        white_mask = cv2.inRange(bgrcap, np.array([1, 1, 1]), np.array([0, 0, 0]))  # special mask for white

        cent = []  # the centers of the facelet-square candidates are stored in this global variable
        if detect ==True:
            find_squares(bgrcap, grid_N)  # find the candidates

            m = medoid(cent)

            cf, ef = facelets(cent, m)  # identify the centers of the corner and edge facelets
            #print(ef,'agfg')

            # compute the alternate corner and edges facelet centers. These are the point reflections of an already
            # known facelet center at the medoid center. Should some facelet center not be detected by itself it usually
            # still is detected in this way.
            acf, aef = mirr_facelet(cf, ef, m)

            vision_params.face_hsv, vision_params.face_col,cents = getcolors(cf, ef, acf, aef, m)
            if len(cents)>4 and validate(cents)<10:
                if vision_params.face_col[4] != last_face[4] and vision_params.face_col in candidate and optical_check:
                    old_points = np.array([cents[4]], dtype=np.float32)
                    point_selected = True
                    #print(move)
                    if len(move)>0:
                        action = np.mean(move,axis=0)
                        action = decide(action)
                        print(action)
                        text = action
                        relation = (last_face, vision_params.face_col, action, problem)
                        
                    last_face = vision_params.face_col
                    move = []
                    config_all = []
                    for i in range(6):
                        config_all.append([])
                
                
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


            for i in cents:
                display_colorname(bgrcap, i)
                
            if point_selected:
                #cv2.circle(bgrcap, m, (0, 0, 255), 2)
                new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame, old_points, None, **lk_params)
                move.append(new_points[0] - old_points[0])
                old_gray = gray_frame.copy()
                old_points = new_points
                x, y = new_points.ravel()
                cv2.circle(bgrcap, (x, y), 5, (0, 255, 0), -1)
                
#             if k == 121:
            if relation is not None:
                temp = problem 
                problem = choose_from(relation)
                print(len(problem))
                if len(problem) == 0:
                    problem = temp
    
        else:
            draw(bgrcap,problem,start,long)
            draw_sol (bgrcap,start,long,solution,step)
            # 'c'
            if k == 99:
                text="Rotate your cube"
                detect =True
                
            # 'n'
            if k == 110:  
                problem = teach(problem, solution,step)
                last_problem = problem
                last_solution = solution
                step += 1
                if step == len(solution.split(' ')):
                    text = " Solved!!!"
                    detect = True
                    

        cv2.putText(bgrcap, text, (100, 50), cv2.FONT_HERSHEY_PLAIN, 4.0, (0, 0, 255), 2)
        
        #cv2.drawContours(bgrcap,final_approx,-1,(0,0,255),3)
        cv2.imshow('color_filter mask', cv2.resize(color_mask, (width // 2, height // 2)))
        cv2.imshow('white_filter mask', cv2.resize(white_mask, (width // 2, height // 2)))
        cv2.imshow('black_filter mask', cv2.resize(black_mask, (width // 2, height // 2)))
        cv2.imshow('Webcam - type "x" to quit.', bgrcap)
        
        flag = True
        for i in range(6):
            if len(config_all[i]) == 0:
                flag = False
                
        if len(problem) == 1:
            solution = kociemba.solve(problem[0])
            text = "Solution found!"

            config_all = []
            for i in range(6):
                config_all.append([])
            print('finished')
            print(solution)
            problem = problem[0]
            detect = False
                
            
        if flag:   
            solution,success,problem = solve(config_all)
            problem = list(set(problem))
            if success>1:
                text = "Candidate Solution found!"
                candidate = produce_can(problem[-1])
                optical_check = True
                print('oh my god', success)
                config_all = []
                for i in range(6):
                    config_all.append([])
            #print(success)
            elif len(solutions) == 0 and success>0:
                problem = problem[0]
                last_problem = problem
                last_solution = solution
                solutions.append(solution)
                text = "Solution found!"
                
                config_all = []
                for i in range(6):
                    config_all.append([])
                print('finished')
                print(solution)
                detect = False
            elif len(solutions) > 0 and success>0:
                if problem == last_problem:
                    solution = last_solution
                    text = 'Right directions and keep on'
                    detect = False
                else:
                    text = 'Move wrong and resolve it'
                    detect =False
                    step = 0
                config_all = []
                for i in range(6):
                    config_all.append([])
                
            
        
        k = cv2.waitKey(5) & 0xFF
        if k == 120:  # type x to exit
            cv2.destroyAllWindows()
            break
            #validate(cents)
            
            
        if k==115:
            final_config = []
            final_config.append(config[3])
            final_config.append(config[1])
            final_config.append(config[0])
            final_config.append(config[4])
            final_config.append(config[2])
            final_config.append(config[5])
            print(final_config)
            solution = solve(final_config)
            print("solution:",solution)
            print(kociemba.solve(solution))


    