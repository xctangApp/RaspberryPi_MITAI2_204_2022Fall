#this is optional

import os
from brachiograph import BrachioGraph
from linedraw import *

inner_arm = 8
outer_arm = 8

bg = BrachioGraph(inner_arm, outer_arm)

if __name__ == "__main__":

    # take photo and save it
    os.system("raspistill -o ~/BrachioGraph/images/cam.jpg")
    # vectorise an image to json file
    image_to_json("cam", draw_contours=2, draw_hatch=16)
    # draw with the plotter
    bg.plot_file("images/cam.json")
