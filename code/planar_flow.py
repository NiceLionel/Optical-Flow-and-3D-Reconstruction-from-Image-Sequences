import numpy as np

def compute_planar_params(flow_x, flow_y, K,
                                up=[256, 0], down=[512, 256]):
    """
    params:
        @flow_x: np.array(h, w)
        @flow_y: np.array(h, w)
        @K: np.array(3, 3)
        @up: upper left index [i,j] of image region to consider.
        @down: lower right index [i,j] of image region to consider.
    return value:
        sol: np.array(8,)
    """
    """
    STUDENT CODE BEGINS
    """
    global A, B
    height = flow_x.shape[0]
    width = flow_y.shape[1]
    K_inverse = np.linalg.inv(K)
    
    upper = up[0]
    lower = down[0]
    right = down[1]
    left = up[1]
    
    # get pixels
    x_prime, y_prime = np.meshgrid(np.arange(left, right), np.arange(upper, lower))
    pixels = np.vstack((x_prime.flatten(), y_prime.flatten(), np.ones(len(x_prime.flatten()))))
    # get calibrated coordinates
    point_calibrate = K_inverse @ pixels
    # get calibrated flow
    xc_flow = flow_x[y_prime, x_prime]
    yc_flow = flow_y[y_prime, x_prime]
    flow_pixel = np.vstack((xc_flow.flatten(), yc_flow.flatten(), np.zeros(len(x_prime.flatten()))))
    flow_calibrated = K_inverse @ flow_pixel
    # get A,b for Ax = b
    for k in range(len(x_prime.flatten())):
        x = point_calibrate[0, k]
        y = point_calibrate[1, k]
        x_cali = flow_calibrated[0, k]
        y_cali = flow_calibrated[1, k]
        a = np.array([[x ** 2, x * y, x, y, 1, 0, 0, 0],
                      [x * y, y ** 2, 0, 0, 0, y, x, 1]])
        b = np.array([x_cali, y_cali]).reshape(-1, 1)
        if k != 0:
            A = np.vstack((A, a))
            B = np.vstack((B, b))
        else:
            A = a
            B = b
        
    # solve Ax = b
    sol = np.linalg.lstsq(A, B, rcond = None)[0].flatten()
    """
    STUDENT CODE ENDS
    """
    return sol
    
