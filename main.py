#!/usr/bin/env python
# -*- coding: utf-8 -*-

from project import *
from cifar import *
from pixel_bags import *

__author__ = "Arunprasath Shankar"
__copyright__ = "Copyright 2013, NEFCIR"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "axs918@case.edu"
__status__ = "Prototype"

nefcir = NEFCIR()
cifar = CIFAR()
cifar.readImages()
cifar.pixels()
cifar.pixelFrequency()
cifar.prevalenceMatrix()

pixel_array = cifar.pixel_array
pixel_row_freq = cifar.pixel_row_freq
pixel_col_freq = cifar.pixel_col_freq
overall_freq = cifar.overall_freq
p_mat = cifar.p_mat

pix = PixelBags(pixel_array, pixel_row_freq, pixel_col_freq, overall_freq, p_mat)
pix.colorBags()
pix.bandBias()
pix.bandPixelBags()
pix.rowBands()