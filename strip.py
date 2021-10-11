def determinant(m):
    if len(m)==0:
        return 0
    elif len(m[0])==2 and len(m)==2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    elif len(m[0])==3:
        return m[0][0] * determinant([[m[1][1], m[1][2]], [m[2][1], m[2][2]]]) - m[0][1] * determinant([[m[1][0], m[1][2]], [m[2][0], m[2][2]]])+ m[0][2] * determinant([[m[1][0], m[1][1]], [m[2][0], m[2][1]]])
    else:
        