import unittest
import test

# Систематизация тестов

testST = unittest.TestSuite()

testST.addTest(unittest.TestLoader().loadTestsFromTestCase(test.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(test.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)
