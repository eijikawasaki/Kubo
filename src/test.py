"""
This module is a test
"""
import numpy as np
import random as rnd
from matplotlib import pyplot as plt


def hello_word():
    """
    Test function
    :return: "hello word"
    """
    print("hello word")


def langevin(gamma, steps, force):
    """
    Langevin theory

    :param gamma:
    :param steps:
    :param force:
    :return:
    """
    tab = []
    v = 0.
    for i in range(steps):
        v += - gamma * v + np.sqrt(2.*gamma)*rnd.gauss(0., 1.) + force
        tab.append(v)
    plt.xlabel("step n")
    plt.ylabel("speed v")
    plt.plot(tab)
    plt.show()
