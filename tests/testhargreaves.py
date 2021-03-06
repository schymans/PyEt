import unittest

import numpy as np
import pandas as pd

import pyet as et


class Testhargreaves(unittest.TestCase):
    def test_hargreaves(self):
        # Based on example 18, p 74 TestFAO56
        tmax = pd.Series([26.6], index=pd.DatetimeIndex(["2015-07-15"]))
        tmin = pd.Series([14.8], index=pd.DatetimeIndex(["2015-07-15"]))
        lat = 45.72 * np.pi / 180
        har = round(et.hargreaves(tmax, tmin, lat), 1)
        self.assertAlmostEqual(har.values, 5.0, 1)
