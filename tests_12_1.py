import test
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        a = test.Runner('Forest Gump')
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    def test_run(self):
        a = test.Runner('Идущий к реке')
        for i in range(10):
            a.run()
        self.assertEqual(a.distance, 100)

    def test_challenge(self):
        a = test.Runner('Мефодий')
        b = test.Runner('Кирилл')
        for i in range(10):
            a.run()
            b.walk()
        self.assertNotEqual(a.distance, b.distance)




if __name__ == '__main__':
    unittest.main()
