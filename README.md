**Optical Flow and 3D Reconstruction from Image Sequences**

## Introduction

In this groundbreaking project, I delve into the intricate realm of optical flow and 3D reconstruction from a sequence of images. At the heart of this exploration is the pursuit to harness the raw information presented in 2D images and translate it into meaningful 3D representations and motion interpretations. 

Throughout the project:

1. **Spatiotemporal Derivatives**: I harness the capabilities of convolution operations to compute the spatiotemporal derivatives, \(Ix\), \(Iy\), and \(It\), using provided Python functions. This foundational step serves as the backbone for further optical flow computations.

2. **Optical Flow Field Generation**: Leveraging the derivatives, I constructed a function to compute the optical flow field. This intricate task involves solving a linear system for each pixel, providing an understanding of the motion between the images.

3. **Vector Field Visualization**: With the optical flow in hand, I implemented a visualization tool to plot the motion vectors. This interactive representation offers insights into the directional flow of motion across the images.

4. **Epipole Calculation**: Venturing into the geometry of the visual scene, I computed the pixel position of the epipole, which is a vital point of intersection for all epipolar lines in the image. Using RANSAC, I efficiently tackled outliers and honed in on the accurate epipolar geometry.

5. **Depth Estimation**: By integrating intrinsic camera parameters and optical flow, I computed a depth map for each pixel. This visualization offers a vivid understanding of the scene's depth dynamics and the relative distances of objects.

6. **Planar Scene Motion Analysis**: Distinguishing the planar parts of the scene, I explored how motion in such areas can be understood and represented through parametrized equations. 

This project is more than just code; it's a journey through the rich landscape of computer vision and its geometric underpinnings. It aims to bridge the gap between 2D images and our 3D understanding of the world.

To get started and explore further, follow the usage instructions below.

## Usage

Please run the code by executing:

    python3 main.py [list of arguments]

After completing each section, you can enable the flag for that part. For instance,
if you are done with depth, you should execute:

    python3 main.py --plot_flow

You can also pass your confidence threshold to the program. For example, if a confidence score of 5 is used, you should execute:

    python3 main.py --depth --threshmin 5


Join me in this immersive dive into the world of image processing and witness how static images can come to life with depth and motion.
