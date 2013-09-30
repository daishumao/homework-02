import unittest
import maxsum
import sys


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.syswrong = [[], ['sss.txt']] 
        self.systrue = [['input_test.txt'], ['\\v','input_test.txt'], ['\\h','input_test.txt'], ['\\a','input_test.txt'], ['\\v','\\h','input_test.txt'], ['\\v','\\h','\\a','input_test.txt']]

    def test_wrong_sys(self):
        for i in range(0, 1):
            sys.argv[1:] = self.syswrong[i]
            self.assertRaises(ValueError, maxsum.main)
    def test_true_sys(self):
        for i in range(0,5):
            sys.argv[1:] = self.systrue[i]
            if i==0:
                self.assertEqual(maxsum.main(), 689)
            elif i==1:
                self.assertEqual(maxsum.main(), 689)
            elif i==2:
                self.assertEqual(maxsum.main(), 753)
            elif i==3:
                self.assertEqual(maxsum.main(), 859)
            elif i==4:
                self.assertEqual(maxsum.main(), 753)
            elif i==5:
                self.assertEqual(maxsum.main(), 859)


if __name__ == '__main__':
    unittest.main()