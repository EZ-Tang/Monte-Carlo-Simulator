"""
Course:  DS 5100
Topic:   Monte Carlo Simulation
Author:  Eric Tang
Date:    15 July 2022
"""


import unittest
import pandas as pd
import numpy as np
from montecarlo import Die, Game, Analyzer

class MonteCarloTestSuite(unittest.TestCase):
    """
    Unit tests for Monte Carlo.
    This class tests all the methods in Die, analyzer, and game class.
    """
    def test_1_init_die(self): 
        """
        Initialize a dice with six faces
        """
        testDie = Die([1, 2, 3, 4, 5, 6])
        self.assertTrue(testDie is not None, "(Test 1) Failed to initalize a dice")


    def test_2_change_weight(self):
        """
        Change the weight of face '6' to a weight of 5.
        """
        testDie = Die([1, 2, 3, 4, 5, 6])
        testDie.change_weight(6, 5)
        self.assertTrue(testDie.show().iloc[5, 1] == 5.0, ("Test 2) Failed to change the weight"))

    def test_3_roll(self):
        """
        Samples the dice roll 20 times and checks if the rolls fall within the appropriate threshold.
        """
        testDie = Die([1, 2, 3, 4, 5, 6])
        self.assertTrue(all(x <= 6 and x >= 1 for x in testDie.roll(20)), ("Test 3) Failed to get the accurate sample of dice roll"))

    def test_4_show(self):
        """
        Creates a test die and an equal representation in a dataframe.
        Checks if the dataframe is equal to the return from show().
        """
        testDie = Die([1, 2, 3, 4, 5, 6])
        equaldf = pd.DataFrame({"face": [1, 2, 3, 4, 5, 6], "weight" : [1.0] * 6})
        self.assertTrue(testDie.show().equals(equaldf), ("Test 4) Failed to accurately show the DataFrame"))

    def test_5_init_game(self):
        """
        Initalize a game with three equal dice.
        """
        testDie = Die([1, 2, 3, 4, 5, 6])
        testGame = Game([testDie, testDie, testDie])
        self.assertTrue(testGame is not None, ("(Test 5) Failed to initalize a game"))

    def test_6_play(self):
        """
        Plays a game with three equal dice .
        Game is played 10 different times.
        """
        testDie = Die([1, 2, 3, 4, 5, 6])
        testGame = Game([testDie, testDie, testDie])
        testGame.play(10)
        self.assertTrue(testGame.show().shape == (10, 3), ("(Test 6) Failed to play the game 10 times."))

    def test_7_show(self):
        """
        Plays a game with three equal dice.
        Game is played 20 different times.
        Checks if the result is shown and within the valid boundaries.
        """
        testDie = Die([1, 2, 3, 4, 5, 6])
        testGame = Game([testDie, testDie, testDie])
        testGame.play(20)
        self.assertTrue(all(x <= 6 and x >= 1 for x in testGame.show().to_numpy().flatten()), ("(Test 7) Failed to accurately display game results."))

    def test_8_init_analyzer(self):
        """
        Initialize an analyzer of a game with two dices of string type.
        """
        testDie = Die(["Apple", "Banana", "Cherry"])
        testGame = Game([testDie, testDie, testDie])
        testAnalyzer = Analyzer(testGame)
        self.assertTrue(testAnalyzer is not None, ("(Test 8) Failed to initalize the analyzer."))

    def test_9_jackpot(self):
        """
        Simulates a game and tests if jackpot results in all faces being identical.
        Game is played 500 times with three dices.
        """
        testDie = Die(["Apple", "Banana", "Cherry", "Seven"])
        testGame = Game([testDie, testDie, testDie])
        testGame.play(500)
        testAnalyzer = Analyzer(testGame)
        testAnalyzer.jackpot()
        result_df = testAnalyzer.jackpot_result
        self.assertTrue(all(result_df[0] == result_df[1]) and all(result_df[0] == result_df[2]), 
            ("(Test 9) Incorrect Jackpot return, dataframe columns are not equal to one another."))

    def test_10_combo(self):
        """
        Simulates a game and the distinct combinations of faces rolled, along with their counts.
        Game is played 25 times with three dices.
        Checks if the combo results in a decreasing order of unique result count.
        """
        testDie = Die(["Apple", "Banana", "Cherry", "Seven", "Blueberry"])
        testGame = Game([testDie, testDie, testDie])
        testGame.play(25)
        testAnalyzer = Analyzer(testGame)
        result_df = testAnalyzer.combo()
        self.assertTrue(result_df['n'].is_monotonic_decreasing, "(Test 10) Combo method does not properly sort unique result count.")

    def test_11_face_counts_per_roll(self):
        """
        Simulates a game and records all roll results in a dataframe.
        Game is played 25 times with three dices.
        Checks if rolls all add up to three for each event.
        """
        testDie = Die(["Apple", "Banana", "Cherry", "Seven", "Blueberry"])
        testGame = Game([testDie, testDie, testDie])
        testGame.play(25)
        testAnalyzer = Analyzer(testGame)
        testAnalyzer.face_counts_per_roll()
        result_df = testAnalyzer.face_per_roll
        result_df['Sum'] = result_df.sum(axis=1)
        self.assertTrue(result_df['Sum'].eq(3).all() , "(Test 11) Total rolls do not properly add up.")

if __name__ == '__main__':
    unittest.main(verbosity=3)