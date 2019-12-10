# CSE 101 - IP HW2
# K-Map Minimization 
# Name: Nikhil Krishnan
# Roll Number: 2018248
# Section: B
# Group: 1
# Date:18/10/18



import unittest
from HW2_2018248 import *



class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual (minFunc("3","() d (0,5,7,1)"),"0")
		self.assertEqual (minFunc("2","(0,1,2) d (3)"),"1")
		self.assertEqual (minFunc("4","() d -"),"0")
		self.assertEqual (minFunc("3","(0,1,3,5) d (6)"),"x'y+w'y+w'x'")
		self.assertEqual (minFunc("4","(0,2,4,6,8,10,12,14) d (1,3,5,7,9,11,13,15)"),"1")
		self.assertEqual (minFunc("4","(0,1,3,4,5,7,13) d (10,14)"),"xy'z+w'z+w'y'")
		self.assertEqual (minFunc("4","(0,1,2,3,5,7,9,13) d -"),"y'z+w'z+w'x'")
		self.assertEqual (minFunc("3","(1,2,6,5) d -"),"xy'+x'y")
		self.assertEqual (minFunc("4","(0,2,5,8,10,15) d (7)"),"xyz+x'z'+w'xz")
		self.assertEqual (minFunc("1","(1) d -"),"w")
		self.assertEqual (minFunc("3","(2,3,6) d (5)"),"xy'+w'x")		
                
if __name__=='__main__':
	unittest.main()
