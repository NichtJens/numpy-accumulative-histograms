#!/usr/bin/env python

import numpy as np


class Hist1D(object):

    def __init__(self, nbins, xlow, xhigh):
        self.nbins = nbins
        self.xlow  = xlow
        self.xhigh = xhigh

        self.range = (xlow, xhigh)

        self.hist, edges = np.histogram([], bins=nbins, range=self.range)
        self.bins = (edges[:-1] + edges[1:]) / 2.

    def fill(self, arr):
        hist, _ = np.histogram(arr, bins=self.nbins, range=self.range)
        self.hist += hist

    @property
    def data(self):
        return self.bins, self.hist


class Hist2D(object):

    def __init__(self, nxbins, xlow, xhigh, nybins, ylow, yhigh):
        self.nxbins = nxbins
        self.xhigh  = xhigh
        self.xlow   = xlow

        self.nybins = nybins
        self.yhigh  = yhigh
        self.ylow   = ylow

        self.nbins  = (nxbins, nybins)
        self.ranges = ((xlow, xhigh), (ylow, yhigh))

        self.hist, xedges, yedges = np.histogram2d([], [], bins=self.nbins, range=self.ranges)
        self.xbins = (xedges[:-1] + xedges[1:]) / 2.
        self.ybins = (yedges[:-1] + yedges[1:]) / 2.

    def fill(self, xarr, yarr):
        hist, _, _ = np.histogram2d(xarr, yarr, bins=self.nbins, range=self.ranges)
        self.hist += hist

    @property
    def data(self):
        return self.xbins, self.ybins, self.hist





if __name__ == "__main__":
    from matplotlib import pyplot as plt

    h = Hist1D(100, 0, 1)
    for _ in range(1000):
        a = np.random.random((3,))
        h.fill(a)
        plt.step(*h.data)
        plt.show()

    h = Hist2D(100, 0, 1, 100, 0, 1)
    for _ in range(1000):
        x, y = np.random.random((3,)), np.random.random((3,))
        h.fill(x, y)
        plt.pcolor(*h.data)
        plt.show()



