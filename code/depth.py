import numpy as np

def depth(flow, confidence, ep, K, thres=10):
    """
    params:
        @flow: np.array(h, w, 2)
        @confidence: np.array(h, w, 2)
        @K: np.array(3, 3)
        @ep: np.array(3,) the epipole you found epipole.py note it is uncalibrated and you need to calibrate it in this function!
    return value:
        depth_map: np.array(h, w)
    """
    depth_map = np.zeros_like(confidence)

    """
    STUDENT CODE BEGINS
    """
    K_inverse = np.linalg.inv(K)

    # get calibrated ep
    Epipole = K_inverse @ ep
    Epipole = (Epipole/Epipole[-1])[0:2].reshape(-1,1)

    Vz = 1
    v_prime = flow[:, :, 1].flatten()
    u_prime = flow[:, :, 0].flatten()
    
    width = confidence.shape[1]
    height = confidence.shape[0]
    

    # get coordinates
    x, y = np.meshgrid(np.arange(0, width), np.arange(0, height))
    # get calibrated coordinates (2xn)
    calibrated_coordinates = K_inverse @ np.vstack((x.flatten(), y.flatten(), np.ones_like(y).flatten()))
    p = calibrated_coordinates[0:2]
    # get p_trans (2xn)
    flow_dot_product = K_inverse @ np.vstack((u_prime, v_prime, np.zeros_like(u_prime)))
    p_transpose = flow_dot_product[0:2]
    # get depth Z
    Z = np.linalg.norm(p - Epipole, axis=0)/np.linalg.norm(p_transpose, axis=0)
    depth_map = Z.reshape(height, width)
    depth_map[confidence < thres] = 0

    """
    STUDENT CODE ENDS
    """

    truncated_depth_map = np.maximum(depth_map, 0)
    valid_depths = truncated_depth_map[truncated_depth_map > 0]
    # You can change the depth bound for better visualization if your depth is in different scale
    depth_bound = valid_depths.mean() + 10 * np.std(valid_depths)
    # print(f'depth bound: {depth_bound}')

    truncated_depth_map[truncated_depth_map > depth_bound] = 0
    truncated_depth_map = truncated_depth_map / truncated_depth_map.max()
    

    return truncated_depth_map
