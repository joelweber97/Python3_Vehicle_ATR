import cv2
import glob
import numpy

"""The goal of this script is to read in random images from a directory into cv2, allow the user to click
in the middle of a vehicle, have cv2 create a bounding box of 22x22 pixels around that point, and extract
that image chip into a new folder which will be used for training a cnn.

top_2016 imagery chips should be 22x22 (or maybe 25x25) pixels to fit most personal vehicles. 

top_2016 imagery has a spatial resolution of .5 meters

"""
