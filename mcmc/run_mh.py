import argparse
import math
import random
import numpy as np
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt
from .mh import MH


def main(args):

    std = math.sqrt(args.var)

    def p_eval(x):

        return 0.3 * math.exp(- 0.2 * x ** 2) + 0.7 * math.exp(- 0.2 * (x - 10) ** 2)

    def p_eval_real(x):

        return 0.3 * (1 / math.sqrt(math.pi * (1 / 0.2))) * math.exp(- 0.2 * x ** 2) + \
               0.7 * (1 / math.sqrt(math.pi * (1 / 0.2))) * math.exp(- 0.2 * (x - 10) ** 2)

    def q_eval(x1, x2):

        return norm.pdf(x1, loc=x2, scale=std)

    def q_sample(x):

        return random.gauss(x, std)

    # run metropolis-hastings
    mh = MH(p_eval, q_eval, q_sample, 0)

    samples = []

    for i in range(args.iters):
        samples.append(mh.step())

    # plot real distribution
    colors = sns.color_palette()

    x = np.linspace(-10, 20, num=1000)
    y = [p_eval_real(xx) for xx in x]
    plt.plot(x, y, c=colors[0])

    # plot samples
    sns.distplot(samples, bins=30, hist=True, norm_hist=True, kde=False, color=colors[0])

    if args.save is not None:
        plt.savefig(args.save, figsize=(2, 1.5), dpi=80)

    if not args.no_show:
        plt.show()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--iters", type=int, default=5000)
    parser.add_argument("--var", type=float, default=100)
    parser.add_argument("--save")
    parser.add_argument("--no-show", default=False, action="store_true")

    parsed = parser.parse_args()
    main(parsed)
