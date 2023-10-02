import math
import pyerf
import random


# source https://statproofbook.github.io/I/ToC#Probability%20Distributions

class UniformDistribution:
    def __init__(self, rand, a, b):
        self.rand = rand
        self.a = a
        self.b = b

    def pdf(self, x):
        if self.a <= x <= self.b:
            return 1 / (self.b - self.a)
        else:
            return 0.0

    def cdf(self, x):
        if x < self.a:
            return 0.0
        elif x >= self.b:
            return 1.0
        else:
            return (x - self.a) / (self.b - self.a)

    def ppf(self, p):
        if 0 <= p <= 1:
            return self.a + p * (self.b - self.a)
        else:
            raise ValueError("p must be between 0 and 1")

    def gen_random(self):
        return self.rand.uniform(self.a, self.b)

    def mean(self):
        return (self.a + self.b) / 2

    def median(self):
        return (self.a + self.b) / 2

    def variance(self):
        # NOTE: test is faulty
        return (math.pow((self.b - self.a), 2)) / 12

    def skewness(self):
        std_dev = math.sqrt(self.variance())
        return 3 * (self.mean() - self.median()) / std_dev  # constant 0

    def ex_kurtosis(self):
        return -6 / 5  # constant value of -1.2

    def mvsk(self):
        if self.a == self.b or self.a >= self.b:
            raise Exception("Moments undefined")
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]


class NormalDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        # NOTE: exceeds error by 0.003
        coeff = 1 / math.sqrt(2 * math.pi * self.scale)
        exponent = -0.5 * (((x - self.loc) ** 2) / (2 * self.scale))
        return coeff * math.exp(exponent)

    def cdf(self, x):
        z = (x - self.loc) / math.sqrt(self.scale * 2)
        return 0.5 * (1 + math.erf(z))

    def ppf(self, p):
        if 0 < p < 1:
            return math.sqrt(2 * self.scale) * pyerf.erfinv(2 * p - 1) + self.loc
        else:
            raise ValueError("p must be in the range (0, 1)")

    def gen_random(self):
        return self.loc + self.scale * math.sqrt(-2 * math.log(self.rand.random())) * math.cos(
            2 * math.pi * self.rand.random())

    def mean(self):
        return self.loc

    def median(self):
        return self.loc

    def variance(self):
        return self.scale

    def skewness(self):
        return 0.0  # The skewness of a normal distribution is always 0

    def ex_kurtosis(self):
        return 0.0  # The kurtosis of a normal distribution is always 0

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]


class CauchyDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        return 1 / (math.pi * self.scale * (1 + ((x - self.loc) / self.scale) ** 2))

    def cdf(self, x):
        return 0.5 + (1 / math.pi) * math.atan((x - self.loc) / self.scale)

    def ppf(self, p):
        if 0 < p < 1:
            return self.loc + self.scale * math.tan(math.pi * (p - 0.5))
        else:
            raise ValueError("p must be in the range (0, 1)")

    def gen_random(self):
        return self.loc + self.scale * math.tan(math.pi * (self.rand.random() - 0.5))

    def mean(self):
        raise Exception("Moment undefined")

    def median(self):
        return self.loc

    def variance(self):
        raise Exception("Moment undefined")

    def skewness(self):
        raise Exception("Moment undefined")

    def ex_kurtosis(self):
        raise Exception("Moment undefined")

    def mvsk(self):
        try:
            return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]
        except:
            raise Exception("Moments undefined")