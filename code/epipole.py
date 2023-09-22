import numpy as np
def epipole(u,v,smin,thresh,num_iterations = 1000):
    ''' Takes flow (u,v) with confidence smin and finds the epipole using only the points with confidence above the threshold thresh 
        (for both sampling and finding inliers)
        params:
            @u: np.array(h,w)
            @v: np.array(h,w)
            @smin: np.array(h,w)
        return value:
            @best_ep: np.array(3,)
            @inliers: np.array(n,) 
        
        u, v and smin are (h,w), thresh is a scalar
        output should be best_ep and inliers, which have shapes, respectively (3,) and (n,) 
    '''

    """
    """
    height,width = u.shape[0], u.shape[1]
    u_valid = u[smin>thresh].flatten()
    v_valid = v[smin>thresh].flatten()
    x_r = np.floor(width/2)
    x_l = -np.ceil(width/2)
    y_up = -np.ceil(height/2)
    y_low = np.floor(height/2)
    x,y = np.meshgrid(np.arange(x_l,x_r),np.arange(y_up,y_low))
    x_valid = x[smin>thresh].flatten()
    y_valid = y[smin>thresh].flatten()
    valid_index = np.arange(0,len(x.flatten()))[smin.flatten()>thresh]
    """ 
    """

    sample_size = 2

    eps = 10**-2

    best_num_inliers = -1
    best_inliers = None
    best_ep = None

    for i in range(num_iterations): #Make sure to vectorize your code or it will be slow! Try not to introduce a nested loop inside this one
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(0,np.sum((smin>thresh))))
        sample_indices = permuted_indices[:sample_size] #indices for thresholded arrays you find above
        test_indices = permuted_indices[sample_size:] #indices for thresholded arrays you find above

        """
        STUDENT CODE BEGINS
        """
        u_sample = u_valid[sample_indices]
        v_sampel = v_valid[sample_indices]
        x_sample = x_valid[sample_indices]
        y_sample = y_valid[sample_indices]
        u_test = u_valid[test_indices]
        v_test = v_valid[test_indices]
        x_test = x_valid[test_indices]
        y_test = y_valid[test_indices]
        
        length = len(test_indices)

  
        epipoles = get_epipole(x_sample, y_sample, u_sample, v_sampel)

        
        inliers = sample_indices
        one_matrix = np.ones(length)
        zero_matrix = np.zeros(length)
        x_prime = np.array([x_test, y_test, one_matrix])
        u_prime = np.array([u_test, v_test, zero_matrix])
        cross_product = np.cross(x_prime, u_prime, axisa=0, axisb=0)
        distances = abs(epipoles @ cross_product.T)
        test_inlier = test_indices[distances < eps]
        inliers = np.concatenate((sample_indices, test_inlier))
        inliers = valid_index[inliers]
        """
        STUDENT CODE ENDS
        """

        #NOTE: inliers need to be indices in flattened original input (unthresholded), 
        #sample indices need to be before the test indices for the autograder
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_ep = epipoles
            best_inliers = inliers


    return best_ep, best_inliers

def get_distance(epipole, x, y, u, v):
    '''

    param ep: epipole (3,)
    param x: (1,)
    param y: (1,)
    param u: (1,)
    param v: (1,)
    return: epT(x X u)
    '''
    xp = (x, y, 1)
    u_prime = (u, v, 0)
    distance = abs(epipole @ np.cross(xp, u_prime))

    return distance

def get_epipole(x, y, u, v):
    '''

    param x: (2,)
    param y: (2,)
    param u: (2,)
    param v: (2,)
    return: epipole (3,)
    '''
    x1 = np.array([x[0], y[0], 1])
    x2 = np.array([x[1], y[1], 1])
    u1 = np.array([u[0], v[0], 0])
    u2 = np.array([u[1], v[1], 0])
    cross_product_1 = np.cross(x1, u1)
    cross_product_2 = np.cross(x2, u2)
    cross_product_xu = np.vstack([cross_product_1, cross_product_2])
    U, S, VT = np.linalg.svd(cross_product_xu)
    epipole = VT.T[:, -1]
    return epipole



