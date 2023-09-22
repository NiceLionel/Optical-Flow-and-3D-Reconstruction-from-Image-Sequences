import numpy as np
import cv2
import pdb
import matplotlib.pyplot as plt
from tqdm import tqdm

def plot_flow(image, flow_image, confidence, threshmin=10):
    """
    params:
        @img: np.array(h, w)
        @flow_image: np.array(h, w, 2)
        @confidence: np.array(h, w)
        @threshmin: confidence must be greater than threshmin to be kept
    return value:
        None
    """

    """
    STUDENT CODE BEGINS
    """
    height, width = image.shape[0], image.shape[1]
    x, y = np.meshgrid(np.arange(0,width),np.arange(0,height))
    flow_x = np.where(confidence>threshmin, flow_image[:,:,0],0)
    flow_y = np.where(confidence>threshmin, flow_image[:,:,1],0)
    # plt.quiver(x,y,(i*10).astype(int),(j*10).astype(int),angles='xy', scale_units='xy', scale=1.,width=0.001, color='red')
    # plt.imshow(image)
    """
    STUDENT CODE ENDS
    """
    
    plt.quiver(x, y, (flow_x * 10).astype(int), (flow_y * 10).astype(int), angles='xy', scale_units='xy', scale=1.,
               width=0.001, color='red')
    plt.imshow(image)
    
    return





    

