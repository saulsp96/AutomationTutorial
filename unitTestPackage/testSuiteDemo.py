import unittest
from unitTestPackage.test_class1 import TestClass1
from unitTestPackage.test_class2 import TestClass2

#Get all test from TestClass1 and TestClass2

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

#create a test suite combining
smoke_test = unittest.TestSuite([tc1,tc2])

#run Testsuite
unittest.TextTestRunner(verbosity=2).run(smoke_test)