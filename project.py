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