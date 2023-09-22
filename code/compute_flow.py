import numpy as np
import pdb

def flow_lk_patch(Ix, Iy, It, x, y, size=5):
    """
    params:
        @Ix: np.array(h, w)
        @Iy: np.array(h, w)
        @It: np.array(h, w)
        @x: int
        @y: int
    return value:
        flow: np.array(2,)
        conf: np.array(1,)
    """
    """

    """
    height, width = Ix.shape[0], Ix.shape[1]
    y_neigh_index = np.array([y - 2, y - 1, y, y + 1, y + 2])
    x_neigh_index = np.array([x - 2, x - 1, x, x + 1, x + 2])

    x_valid_mask = np.logical_and(x_neigh_index>=0, x_neigh_index<width)
    y_valid_mask = np.logical_and(y_neigh_index>=0, y_neigh_index<height)
    x_valid_neigh_index = x_neigh_index[x_valid_mask]
    y_valid_neigh_index = y_neigh_index[y_valid_mask]

    dIx = Ix[y_valid_neigh_index,:][:,x_valid_neigh_index].reshape(-1,1)
    dIy = Iy[y_valid_neigh_index,:][:,x_valid_neigh_index].reshape(-1,1)
    dIt = It[y_valid_neigh_index,:][:,x_valid_neigh_index].reshape(-1,1)

    A = np.concatenate((dIx,dIy),axis = 1)
    b = -dIt
    x,_,_,s = np.linalg.lstsq(A,b,rcond=None)
    flow = x.reshape(2,)
    conf = np.min(s)
    """

    """
    return flow, conf


def flow_lk(Ix, Iy, It, size=5):
    """
    params:
        @Ix: np.array(h, w)
        @Iy: np.array(h, w)
        @It: np.array(h, w)
    return value:
        flow: np.array(h, w, 2)
        conf: np.array(h, w)
    """
    image_flow = np.zeros([Ix.shape[0], Ix.shape[1], 2])
    confidence = np.zeros([Ix.shape[0], Ix.shape[1]])
    for x in range(Ix.shape[1]):
        for y in range(Ix.shape[0]):
            flow, conf = flow_lk_patch(Ix, Iy, It, x, y)
            image_flow[y, x, :] = flow
            confidence[y, x] = conf
    return image_flow, confidence

    

