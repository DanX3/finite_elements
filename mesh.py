import numpy as np

def read_msh(filename):

    """ read mesh code """
    meshfile = open(filename, 'r')
    x = np.array([])
    y = np.array([])
    b_nodes = []
    topo = np.array([], dtype=np.int_)
    for line in meshfile:
        if line[0] == '$':
            continue
        
        #here something has to happen
        l = map(float, line.split())
        if len(l) == 4:
            x = np.append(x, l[1])
            y = np.append(y, l[2])
        if len(l) == 7:
            #bnodes
            nodes = l[5:]
            for i in nodes:
                i = int(i) - 1
                if i not in b_nodes:
                    b_nodes.append(i)
            ##check to not overlap them
            # i'm interested in the last 2 numbers
        if len(l) == 8:
            #topo
            ##check to not overlap them
            nd = map(int, l[5:])
            topo = np.append(topo, nd)
            # i'm interested in the last 3 numbers
    meshfile.close()
            
    b_nodes = np.array(b_nodes)
    topo = topo - 1
    #print topo.shape
    topo = np.reshape(topo, (len(topo)/3, 3))

    r_id = 0
    for row in topo:
        ck =      (x[row[1]]-x[row[0]])*(y[row[2]]-y[row[0]])
        ck = ck - (x[row[2]]-x[row[0]])*(y[row[1]]-y[row[0]])
        if ck < 0:
            topo[r_id,:] = np.array([[row[0],row[2],row[1]]])
        r_id+=1

    #print r_id
    nodes = []
    return topo , x , y , nodes , b_nodes
