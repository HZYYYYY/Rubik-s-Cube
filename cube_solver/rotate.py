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