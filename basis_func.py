import numpy as np

def tri_p1(x,y,eval_p):
    """
    Linear shape function on triangles, namely p1.

    Input:

    x : one dimensional array of triangle vertices x coords.\n
    y : one dimensional array of triangle vertices y coords.\n
    eval_p: (n,2) array of the n evaluation points. first
            column indicates x-coord, second y-coord.\n

    Output:

    dx_phi : the three x-derivatives.\n
    dy_phi : the three y-derivatives.\n
    phi    : (n,3) array of the three shape functions at the n eval points.\n
    surf_e : the triangle area.\n

    Notice: all the quantities are computed on the current element

    """
    # evaluate coefficients
    A = np.array([[x[0],y[0],1], [x[1],y[1],1], [x[2],y[2],1]])

    b1 = np.array([1,0,0])
    b2 = np.array([0,1,0])
    b3 = np.array([0,0,1])

    c1 = np.linalg.solve(A, b1) 
    c2 = np.linalg.solve(A, b2) 
    c3 = np.linalg.solve(A, b3) 

    # compute the values of phi's

    phi = np.zeros((eval_p.shape[0],3))

    for i in range(0, eval_p.shape[0]):
        phi[i][0] = c1[0]*eval_p[i][0] + c1[1]*eval_p[i][1] + c1[2]
        phi[i][1] = c2[0]*eval_p[i][0] + c2[1]*eval_p[i][1] + c2[2]
        phi[i][2] = c3[0]*eval_p[i][0] + c3[1]*eval_p[i][1] + c3[2]

    dx_phi = np.array([c1[0],c2[0],c3[0]])
    dy_phi = np.array([c1[1],c2[1],c3[1]])

    surf_e = .5*np.linalg.det(A)

    return dx_phi,dy_phi,phi[0],surf_e

