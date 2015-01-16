# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 11:42:28 2015

@author: David
"""
from __future__ import print_function
import glob
import numpy as np


def dataReader(pattern):
    """ The following function reads all data type specified for analysis
    """
    for file in glob.glob(pattern):
        print("Reading file...", file)
        data=np.genfromtxt(file, delimiter=',', missing_values='0')
        return data
if __name__=="__main__":
    dataReader(pattern)