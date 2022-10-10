import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
import pandas as pd

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'new_function']
# __all__ = [...]


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def new_function(x):
    return pd.date_range("20130101", periods=x)
