<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from webcolors import rgb_to_name, css3_hex_to_names, hex_to_rgb
__author__ = "Arunprasath Shankar"
__copyright__ = "Copyright 2013, NEFCIR"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "axs918@case.edu"
__status__ = "Prototype"


class NEFCIR(object):
    def __init__(self):
        """
        Neuro-fuzzy Content based Information Retrieval
        A novel Neuro-fuzzy approach for CBIR


        """
        pass

    def closest_color(self, requested_color):

        min_colors = {}
        for key, name in css3_hex_to_names.items():
            r_c, g_c, b_c = hex_to_rgb(key)
            rd = (r_c - requested_color[0]) ** 2
            gd = (g_c - requested_color[1]) ** 2
            bd = (b_c - requested_color[2]) ** 2
            min_colors[(rd + gd + bd)] = name
        return min_colors[min(min_colors.keys())]
    
    def get_color_name(self, requested_color):
        try:
            closest_name = rgb_to_name(requested_color)
        except ValueError:
            closest_name = self.closest_color(requested_color)
        return closest_name

    def chunks(self, l, n):
        """ Yield successive n-sized chunks from l.
        """
        for i in xrange(0, len(l), n):
            yield l[i:i + n]
=======
from webcolors import rgb_to_name, css3_hex_to_names, hex_to_rgb
from scipy.misc import imread, imsave, imshow, imfilter
import matplotlib.pyplot as plt
import cPickle as pickle
import numpy as np
import Image


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in css3_hex_to_names.items():
        r_c, g_c, b_c = hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

with open('./cifar-10-batches-py/data_batch_1') as fp:
    batch_data = pickle.load(fp)
    for i, im in enumerate(batch_data['data']):
        if not (i + 1) > 20:
            rgb = list(chunks(list(im), 1024))
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]
            red_rows = list(chunks(red, 32))
            green_rows = list(chunks(green, 32))
            blue_rows = list(chunks(blue, 32))

            rgb_stacked = np.dstack((red_rows, green_rows, blue_rows))
            print rgb_stacked
            r = Image.fromarray(rgb_stacked)
            image_name = str(batch_data['filenames'][i]) + '.png'
            r.save(image_name)
            pixels = []
            rgb = []
            for red, green, blue in zip(red_rows, green_rows, blue_rows):
                for r, g, b in zip(red, green, blue):
                    #rgb.append([r, g, b, get_colour_name(tuple([r, g, b]))])
                    rgb.append([r, g, b])
                pixels.append(rgb)
            #print pixels
            print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n'





#imsave('riri_scaled.jpg', scaled_im)
#plt.imshow(scaled_im)
#plt.show()
>>>>>>> 624b150a01f5a9a82be206eb6039412e92094ad5
