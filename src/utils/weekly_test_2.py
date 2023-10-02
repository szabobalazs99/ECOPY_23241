import math
import pyerf
import random


class LaplaceDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        return 1.0 / (2.0 * self.scale) * math.exp(-abs(x - self.loc) / self.scale)

    def cdf(self, x):
        if x < self.loc:
            return 0.5 * math.exp((x - self.loc) / self.scale)
        else:
            return 1 - 0.5 * math.exp(-((x - self.loc) / self.scale))

    def ppf(self, p):
        if p < 0.5:
            return self.loc + self.scale * math.log(2 * p)
        else:
            return self.loc - self.scale * math.log(2 - 2 * p)

    def gen_rand(self):
        u = self.rand.random()
        if u < 0.5:
            return self.loc + self.scale * math.log(2 * u)
        else:
            return self.loc - self.scale * math.log(2 - 2 * u)

    def mean(self):
        return self.loc

    def median(self):
        return self.loc

    def variance(self):
        return 2 * self.scale ** 2

    def skewness(self):
        return 0.0

    def ex_kurtosis(self):
        return 3.0

    def mvsk(self):
        try:
            return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]
        except:
            raise Exception("Moments undefined")


class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

    def pdf(self, x):
        if x >= self.scale:
            return (self.shape * (self.scale ** self.shape)) / (x ** (self.shape + 1))
        else:
            return 0.0

    def cdf(self, x):
        if x >= self.scale:
            return 1.0 - (self.scale / x) ** self.shape
        else:
            return 0.0

    def ppf(self, p):
        if 0 < p <= 1:
            return self.scale / (1 - p) ** (1 / self.shape)
        else:
            raise ValueError("p must be in the range (0, 1]")

    def gen_rand(self):
        random_number = random.paretovariate(self.shape)
        return self.scale * random_number

    def mean(self):
        if self.shape <= 1:
            return math.inf
        else:
            return (self.shape * self.scale) / (self.shape - 1)

    def variance(self):
        if self.shape <= 2:
            return math.inf
        else:
            return (self.scale ** 2 * self.shape) / ((self.shape - 1) ** 2 * (self.shape - 2))

    def skewness(self):
        if self.shape <= 3:
            return math.inf
        else:
            return (2 * (1 + self.shape)) / (self.shape - 3) * math.sqrt((self.shape - 2) / self.shape)

    def ex_kurtosis(self):
        if self.shape <= 4:
            return math.inf
        else:
            return 6 * ((self.shape ** 3 + self.shape ** 2 - 6 * self.shape - 2) / (
                    self.shape * (self.shape - 3) * (self.shape - 4)))

    def mvsk(self):
        try:
            return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]
        except:
            raise Exception("Moments undefined")