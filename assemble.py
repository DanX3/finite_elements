from basis_func import *
import numpy as np

def gradu_gradv(topo,x,y):
    """ A assembly code """
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
