import main
import unittest


class TournamentTest(unittest.TestCase):


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

    def test_US_NK(self):
        tournament = main.Tournament(90, self.runner1, self.runner3)    # Объект соревнования
        results = tournament.start()        # Результаты соревнования
        TournamentTest.all_results['test_US_NK'] = {k: str(v) for k, v in results.items()}  # Сохраняем результаты тестов
        self.assertTrue(results[max(results.keys())] == 'Ник')    #проверяем чтоб ник был последним     # с результатами соревнования в словарь

    def test_AN_NK(self):
        tournament = main.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results['test_AN_NK'] = {k: str(v) for k, v in results.items()}
        self.assertTrue(results[max(results.keys())] == 'Ник')

    def test_US_AN_NK(self):
        tournament = main.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results['test_US_AN_NK'] = {k: str(v) for k, v in results.items()}
        self.assertTrue(results[max(results.keys())] == 'Ник')

if __name__ == '__main__':
    unittest.main()
