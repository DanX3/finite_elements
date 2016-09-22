import numpy as np

from mesh import *
from basis_func import *
from assemble import *

from viewer import *


def clear_rows(A,b_nodes):
    """ code to clear rows """
    for node in b_nodes:
        t = A[node, node] 
        A[node, :] = 0
        A[node, node]=t


if __name__ == "__main__":

    (topo , x , y , nodes , b_nodes) = read_msh("mesh/square.msh")

    # compute A
    A = gradu_gradv(topo,x,y)
    clear_rows(A,b_nodes)

    # compute rhs
    F = f_v(topo,x,y)
    F[b_nodes] = 0

    # solve linear system Au=F
    u = np.linalg.solve(A, F) 


    plot_sol_p1(x,y,u,topo)


