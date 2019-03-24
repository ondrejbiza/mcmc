import math
import random
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt
from .mh import MH


std = math.sqrt(100)


def p_eval(x):

    return 0.3 * math.exp(- 0.2 * x ** 2) + 0.7 * math.exp(- 0.2 * (x - 10) ** 2)


def q_eval(x1, x2):

    return norm.pdf(x1, loc=x2, scale=std)


def q_sample(x):

    return random.gauss(x, std)


mh = MH(p_eval, q_eval, q_sample, 0)

samples = []

for i in range(5000):
    samples.append(mh.step())

sns.distplot(samples)
plt.show()
