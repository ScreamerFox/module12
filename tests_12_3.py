import main
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        a = main.Runner('Forest Gump')
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        a = main.Runner('Идущий к реке')
        for i in range(10):
            a.run()
        self.assertEqual(a.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        a = main.Runner('Мефодий')
        b = main.Runner('Кирилл')
        for i in range(10):
            a.run()
            b.walk()
        self.assertNotEqual(a.distance, b.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):

        cls.all_results = {}

    def setUp(self):
        self.runner1 = main.Runner('Усейн', 10)
        self.runner2 = main.Runner('Андрей', 9)
        self.runner3 = main.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'Тест {key}: {value}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_US_NK(self):
        tournament = main.Tournament(90, self.runner1, self.runner3)    # Объект соревнования
        results = tournament.start()        # Результаты соревнования
        TournamentTest.all_results['test_US_NK'] = {k: str(v) for k, v in results.items()}  # Сохраняем результаты тестов
        self.assertTrue(results[max(results.keys())] == 'Ник')    #проверяем чтоб ник был последним     # с результатами соревнования в словарь

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_AN_NK(self):
        tournament = main.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results['test_AN_NK'] = {k: str(v) for k, v in results.items()}
        self.assertTrue(results[max(results.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_US_AN_NK(self):
        tournament = main.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results['test_US_AN_NK'] = {k: str(v) for k, v in results.items()}
        self.assertTrue(results[max(results.keys())] == 'Ник')
