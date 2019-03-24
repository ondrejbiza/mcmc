# Metropolis-Hastings algorithm
import random


class MH:

    def __init__(self, p_eval, q_eval, q_sample, init):

        self.p_eval = p_eval
        self.q_eval = q_eval
        self.q_sample = q_sample
        self.init = init
        self.x = init

    def step(self):

        new_x = self.q_sample(self.x)
        a = self.acceptance(new_x)
        u = random.uniform(0, 1)

        if u < a:
            self.x = new_x

        return self.x

    def reset(self):

        self.x = self.init

    def acceptance(self, new_x):

        term1 = self.p_eval(new_x) * self.q_eval(self.x, new_x)
        term2 = self.p_eval(self.x) * self.q_eval(new_x, self.x)

        return min(1, term1 / term2)
