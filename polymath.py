from scipy.integrate import quad


class Polymath:
    def integrand(self, x):
        return 4 * x ** 2 - 1

    def integrate(self, a, b):
        return quad(self.integrand, a, b)
