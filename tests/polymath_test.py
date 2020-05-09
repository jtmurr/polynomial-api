import math
import unittest

from polymath import Polymath


class TestPolymath(unittest.TestCase):
    def test_integrate(self):
        pm = Polymath()

        y, err = pm.integrate(0, 1)

        self.assertTrue(math.isclose(y, 0.333333, abs_tol=0.6))
        self.assertTrue(math.isclose(err, 0.0, abs_tol=0.6))
