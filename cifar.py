#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from operator import itemgetter
from itertools import groupby
from project import NEFCIR
import numpy as np
import pickle
import Image

__author__ = "Arunprasath Shankar"
__copyright__ = "Copyright 2013, NEFCIR"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "axs918@case.edu"
__status__ = "Prototype"


class CIFAR(NEFCIR):
    def __init__(self):
        super(CIFAR, self).__init__()
        self.pixel_row_freq = {}
        self.pixel_col_freq = {}
        self.p_mat = []

    def readImages(self):
        classes = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                   'dog', 'frog', 'horse', 'ship', 'truck']
        with open('./cifar-10-batches-py/data_batch_1') as batch:
            batch_data = pickle.load(batch)
            for i, image in enumerate(batch_data['data']):
                if i == 13:  # gate for image index choice
                    print batch_data['batch_label'], classes[batch_data['labels'][i]]
                    rgb = list(NEFCIR.chunks(self, list(image), 1024))
                    red = rgb[0]
                    green = rgb[1]
                    blue = rgb[2]
                    #print red, green, blue
                    self.red_32x32 = list(NEFCIR.chunks(self, red, 32))
                    self.green_32x32 = list(NEFCIR.chunks(self, green, 32))
                    self.blue_32x32 = list(NEFCIR.chunks(self, blue, 32))
                    rgb_stack_32x32 = np.dstack((self.red_32x32, self.green_32x32, self.blue_32x32))
                    im = Image.fromarray(rgb_stack_32x32)
                    image_name = str(classes[batch_data['labels'][i]]) + '_' + str(batch_data['filenames'][i])
                    im.save(image_name)

    def pixels(self):
        pixels = []
        for i, (red, green, blue) in enumerate(zip(self.red_32x32, self.green_32x32, self.blue_32x32)):
            rgb_im = []
            for j, (r, g, b) in enumerate(zip(red, green, blue)):
                rgb_im.append([(i + 1, j + 1), r, g, b, NEFCIR.get_color_name(self, tuple([r, g, b]))])
            pixels.append(rgb_im)
        pixel_array = []
        for pixel in pixels:
            pixel_array.append(np.array(pixel))
        self.pixel_array = np.array(pixel_array)

    def colorFreq(self, lst):
        cf = {}
        lst = sorted(lst, key=itemgetter(4))
        for k, v in groupby(np.array(lst), key=lambda x: x[4]):
            cf[k] = len(list(v)) / len(lst)
        return cf

    def pixelFrequency(self):
        self.overall_freq = []
        # traverse row for pixel prevalence
        for i in range(len(self.pixel_array)):
            self.pixel_row_freq[i + 1] = self.colorFreq(self.pixel_array[i])

        # traverse column for pixel prevalence
        for i in range(len(self.pixel_array)):
            column_colors = []
            for j in range(len(self.pixel_array)):
                column_colors.append(self.pixel_array[j, i])
                self.overall_freq.append(self.pixel_array[j, i])
            self.pixel_col_freq[i + 1] = self.colorFreq(column_colors)

    def prevalenceMatrix(self):
        for i in range(len(self.pixel_array)):
            for j in range(len(self.pixel_array)):
                self.p_mat.append([self.pixel_array[i, j][4], 1 - (
                    self.pixel_row_freq[self.pixel_array[i, j][0][0]][self.pixel_array[i, j][4]] *
                    self.pixel_col_freq[self.pixel_array[i, j][0][1]][self.pixel_array[i, j][4]] *
                    self.colorFreq(self.overall_freq)[self.pixel_array[i, j][4]])])
        self.p_mat = sorted(self.p_mat, key=itemgetter(1))
        max_p_mat = self.p_mat[-1][1]
        # normalizing prevalence matrix
        self.p_mat = [[x[0], x[1] / max_p_mat] for x in self.p_mat]
        self.p_mat = sorted(self.p_mat, key=itemgetter(0))



