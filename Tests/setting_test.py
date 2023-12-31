import unittest
from DurakAIGame.player import Player
from DurakAIGame.initialize import get_user_settings, initialize_players, InvalidDirectionError


class TestDurakGame(unittest.TestCase):
    def test_get_user_settings(self):
        test_cases = [
            (4, 6, 1),
            (3, 5, 2),
            (2, 4, 3),
        ]
        expected_results = [
            (4, 6, 1),
            (3, 5, 2),
            InvalidDirectionError,
        ]

        for test_case, expected_result in zip(test_cases, expected_results):
            with self.subTest(test_case=test_case, expected_result=expected_result):
                if expected_result == InvalidDirectionError:
                    with self.assertRaises(InvalidDirectionError) as context:
                        result = get_user_settings(*test_case)
                        self.assertEqual(result, (4, 6, 1))
                    self.assertIn("Invalid direction!", str(context.exception))
                else:
                    result = get_user_settings(*test_case)
                    self.assertEqual(result, expected_result)

    def test_initialize_players(self):
        test_cases = [4, 3, 2]  # Add more test cases as needed

        for num_players in test_cases:
            with self.subTest(num_players=num_players):
                players = initialize_players(num_players, Player)
                self.assertEqual(len(players), num_players)

                for player in players:
                    self.assertIsInstance(player, Player)


if __name__ == '__main__':
    unittest.main()
