from basis_func import *
import numpy as np

def gradu_gradv(topo,x,y):
    """ A assembly code """
    print topo
    A = np.zeros((x.shape[0], x.shape[0]))
    print A
    print x

    for element in topo:
        print element
        x_l = x[element]
        y_l = y[element]

        print x_l

        (dx_phi, dy_phi, phi, surf_e) = tri_p1(x_l, y_l, np.zeros((1, 2)))
        local_A = np.zeros((3, 3))
        for i in range(0, 3):
            for j in range(0,3):
                local_A[i, j] = surf_e * \
                (dx_phi[i]*dx_phi[j] + dy_phi[i]*dy_phi[j])

        for i in range(0, 3):
            for j in range(0,3):
                A[element[i], element[j]] += local_A[i,j]
    return A

def f_v(topo,x,y):
    """ F assembly code """
    F = np.zeros((x.shape[0]))

    for element in topo:
        x_l = x[element]
        y_l = y[element]
        (dx_phi, dy_phi, phi, surf_e) = tri_p1(x_l, y_l, np.zeros((1,2)))       
        for vertex in element:
            F[vertex] += surf_e / 3. 

    return F
