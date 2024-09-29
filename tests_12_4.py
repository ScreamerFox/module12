import main
import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', encoding='UTF-8', filename='runner_tests.log',
                        format='%(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            a = main.Runner('Forest Gump', -10)
            for i in range(10):
                a.walk()
            self.assertEqual(a.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            a = main.Runner('Идущий к реке', abraham)
            for i in range(10):
                a.run()
            self.assertEqual(a.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except NameError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        a = main.Runner('Мефодий')
        b = main.Runner('Кирилл')
        for i in range(10):
            a.run()
            b.walk()
        self.assertNotEqual(a.distance, b.distance)




if __name__ == '__main__':
    unittest.main()
