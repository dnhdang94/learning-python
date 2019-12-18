import sys
import os
import unittest

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))
from src.hashutils import *

resrc_path = 'resrc_test.png'

class MyTest(unittest.TestCase):
    def test_md5(self):
        self.assertEqual(compute_file_md5_hexdigest(resrc_path).lower(), '0343616ECD32CF13D77D4EDC1CAC0E4A'.lower())

    def test_sha1(self):
        self.assertEqual(compute_file_sha1_hexdigest(resrc_path).lower(), '5915CDE7DCDEE9259D858C222FA2226E8CE162DC'.lower())

    def test_sha256(self):
        self.assertEqual(compute_file_sha256_hexdigest(resrc_path).lower(), 'E5211E75BACA9B96ED7C8D598D6295A980AF2B76A9DA5EED6F35F102C7C46F1D'.lower())

if __name__ == '__main__':
    unittest.main()
