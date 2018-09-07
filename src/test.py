"""
This module is a test
"""
import numpy as np
import random as rnd
from matplotlib import pyplot

def hello_word():
    """
    Test function
    :return: "hello word"
    """
    print("hello word")



gamma = 1.
v = 1.
force = 1.
tab = []

for i in range(1000):
    v = v - gamma * v + np.sqrt(2.*gamma)*rnd.random() + force
    tab.append(v)


pyplot.plot(tab)
pyplot.show()