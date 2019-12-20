import sys
import os
import unittest

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))
from src.vtutils import *

# Fill your API key here!
apikey = ''

class MyTest(unittest.TestCase):
    def test_md5(self):
        self.assertEqual(is_valid_apikey(apikey), True)

if __name__ == '__main__':
    unittest.main()
