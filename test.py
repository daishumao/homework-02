import unittest
import maxsum
import sys


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.syswrong = [[], ['sss.txt']] 
        self.truewrong = [['input.txt'], ['\v','input.txt'], ['\h','input.txt'], ['\a','input.txt'], ['\v','\h','input.txt'], ['\v','\h','\a','input.txt']]

    def test_wrong_sys(self):
        for i in range(0, 2):
            sys.argv[1:] = self.syswrong[i]
            self.assertRaises(ValueError, homework02.main)
    def test_true_sys(self):
        for i in range(0,6):
            if i==0:
                self.assertEqual(maxsum.main(), 1221)
            elif i==1:
                self.assertEqual(maxsum.main(), 1221)
            elif i==2:
                self.assertEqual(maxsum.main(), 1221)
            elif i==3:
                self.assertEqual(maxsum.main(), 1221)
            elif i==4:
                self.assertEqual(maxsum.main(), 1498)
            elif i==5:
                self.assertEqual(maxsum.main(), 1498)


if __name__ == '__main__':
    unittest.main()