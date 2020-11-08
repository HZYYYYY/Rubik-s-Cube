
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
    return ['1','2']