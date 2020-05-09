from scipy.integrate import quad


class Polymath:
    @classmethod
    def integrand(cls, x):
        return 4 * x ** 2 - 1

    @classmethod
    def integrate(cls, a, b):
        return quad(cls.integrand, a, b)
