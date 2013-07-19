#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from itertools import groupby
from cifar import CIFAR

__author__ = "Arunprasath Shankar"
__copyright__ = "Copyright 2013, NEFCIR"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "axs918@case.edu"
__status__ = "Prototype"


class PixelBags(CIFAR):
    def __init__(self, pixel_array, pixel_row_freq, pixel_col_freq, overall_freq, p_mat):
        super(PixelBags, self).__init__()
        self.pixel_array = pixel_array
        self.pixel_row_freq = pixel_row_freq
        self.pixel_col_freq = pixel_col_freq
        self.overall_freq = overall_freq
        self.p_mat = p_mat

    def colorBags(self):
        # color freqs -> base metric analogous to tf-idf in NEFCIS
        color_freqs = []
        color_bags = {}
        for color, info in groupby(self.p_mat, key=lambda x: x[0]):
            info = list(info)
            for item in info:
                color_freqs.append(item[1])
            color_bags[color] = list(set(color_freqs))  # color bags as python dict with color frequencies as a list

    def bandBias(self):
        band_bias = {}
        if len(self.pixel_array) % 2 == 0:
            focus_band_left = len(self.pixel_array) // 2  # mid band left
            focus_band_right = (len(self.pixel_array) // 2) + 1  # mid band right

            # row band bias
            for i in range(len(self.pixel_array)):
                if i + 1 < focus_band_left:
                    bias = (i + 1) / focus_band_left
                    band_bias[i + 1] = bias
                elif i + 1 > focus_band_right:
                    bias = 1 - (((i + 1) - focus_band_right) / focus_band_right)
                    band_bias[i + 1] = bias
                else:
                    bias = 1
                    band_bias[i + 1] = bias

    def bandPixelBags(self):
        self.band_pixels = []
        for i in range(len(self.pixel_array)):
            for j in range(len(self.pixel_array)):
                self.band_pixels.append([self.pixel_array[i, j][0][0], self.pixel_array[i, j][0][1], 1 - (
                    self.pixel_row_freq[self.pixel_array[i, j][0][0]][self.pixel_array[i, j][4]] *
                    self.pixel_col_freq[self.pixel_array[i, j][0][1]][self.pixel_array[i, j][4]] *
                    CIFAR.colorFreq(self, self.overall_freq)[self.pixel_array[i, j][4]])])
                #print self.band_pixels

    def rowBands(self):
        row_freqs = []
        row_bands = {}
        for row, info in groupby(self.band_pixels, key=lambda x: x[0]):
            info = list(info)
            for item in info:
                row_freqs.append(item[2])
            row_bands[row] = list(set(row_freqs))

    def colBands(self):
        col_freqs = []
        col_bands = {}
        for col, info in groupby(self.band_pixels, key=lambda x: x[0]):
            info = list(info)
            for item in info:
                col_freqs.append(item[2])
            col_bands[col] = list(set(col_freqs))

    def foo(self):
        pass