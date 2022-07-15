"""
Course:  DS 5100
Topic:   Monte Carlo Simulation
Author:  Eric Tang
Date:    15 July 2022
"""


import numpy as np
import pandas as pd

class Die:
    """
    Die with N sides, or “faces”, and W weights, and can be rolled to select a face. 
    """

    def __init__(self, faces):
        """     
        Takes an array of faces as an argument, data type may be strings or numbers.
        Initializes the weights to 1.0 for each face.
        Saves both faces and weights into a private dataframe.
        """
        self.__df = pd.DataFrame({"face": faces, "weight" : [1.0] * len(faces)})

    def change_weight(self, face, weight):
        """     
        Takes two arguments: the face value to be changed and the new weight.
        Checks if the face passed is valid and if the weight is valid.
        Changes the weight of a single side.
        """
        if face not in self.__df.face.values:
            raise ValueError("Face value not in list!")
        if not (isinstance(weight, float) or isinstance(weight, int)):
            raise TypeError("Weight is not a valid number!")
        row_index = self.__df.index[self.__df['face'] == face]
        self.__df.loc[row_index, 'weight'] = weight

    def roll(self, r = 1):
        """
        Takes a parameter of how many times the die is to be rolled; defaults to 1. 
        Essentially a random sample from the vector of faces according to the weights.
        Returns a list of outcomes
        """
        return (self.__df['face'].sample(n = r, weights = self.__df['weight'], replace = True)).tolist()

    def show(self):
        """
        Returns  the die's current set of faces and weights
        """
        return self.__df

class Game:
    """
    A game consisting of rolling one or more dice of the same kind one or more times
    """

    def __init__(self, dice = []):
        """
        Takes a single parameter, a list of already instantiated similar Die objects
        """
        self.dice = dice

    def play(self, n = 1):
        """
        Takes a parameter to specify how many times the dice should be rolled.
        Saves the result of the play to a private dataframe of shape N rolls by M dice.
        The private dataframe should have the roll number is a named index.
        """
        self.__result = pd.DataFrame()
        for r in self.dice:
            self.__result = pd.concat([self.__result, pd.DataFrame(r.roll(n))], axis = 1, ignore_index=True)
        self.__result = self.__result.rename_axis(index='Roll', columns = 'Dice')

    def show(self, form = 'wide'):
        """
        Takes a parameter to return the dataframe in narrow or wide form, defaulting to wide form.
        Exception is raised if the user passes an invalid option.
        Narrow form is a two-column index with the roll number and the die number, and a column for the face rolled.
        Wide form is a single column index with the roll number, and each die number as a column.
        """
        try:
            if form == 'wide':
                return self.__result
            elif form == 'narrow':
                return self.__result.stack()
            raise ValueError("Please pass a valid string ('narrow' or 'wide').")
        except:
            raise AttributeError("No result exist. Please play the game first!")

class Analyzer:
    """
    Analyzer takes the results of a single game and computes various descriptive statistical properties. 
    These properties results are available as attributes of an Analyzer object.
    """

    def __init__(self, game):
        """
        Takes a game object as its input parameter. 
        At initialization time, it records the data type of the die faces used.
        (Optionally) can also call and record the properties without the user explicitly calling the method.
        """
        self.game = game
        self.gameType = type(game.dice[0].show()["face"].iloc[0]) # records the face data type of the dice in game
        # self.jackpot_results = self.jackpot()
        # self.result = self.combo()
        # self.face_per_roll = self.face_counts_per_roll()

    def jackpot(self):
        """
        Computes how many times the game resulted in all faces being identical.
        Stores the results as a dataframe of jackpot results in a public attribute.
        Returns an integer for the number times.
        """
        self.jackpot_result = self.game.show()[(self.game.show()).nunique(axis = 1) == 1]
        return (len(self.jackpot_result.index))

    def combo(self):
        """
        Computes the distinct combinations of faces rolled, along with their counts.
        Combinations is sorted and saved as a multi-columned index.
        Stores the results as a dataframe in a public attribute.
        Returns the dataframe of results
        """
        self.combo_result = self.game.show().apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('n')
        return self.combo_result

    def face_counts_per_roll(self):
        """
        Computes how many times a given face is rolled in each event.
        Stores the results as a dataframe in a public attribute.
        Dataframe has an index of the roll number and face values as columns.
        Returns the dataframe of results.   
        """
        self.face_per_roll = pd.DataFrame(self.game.show().iloc[x].value_counts() for x in range(0, len(self.game.show())))
        self.face_per_roll = self.face_per_roll.fillna(0).astype(int).rename_axis(index='Roll', columns = 'Face') # renaming axis and converting NaN to 0s
        return self.face_per_roll