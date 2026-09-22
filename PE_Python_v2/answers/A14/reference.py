import numpy as np
def load_scores(path):
    return np.loadtxt(path,delimiter=",",skiprows=1,usecols=[1,2],ndmin=2)
def load_missing(path):
    return np.genfromtxt(path,delimiter=",",skip_header=1,filling_values=-1,ndmin=2)
