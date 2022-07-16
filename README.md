# Monte Carlo Simulator
A Monte Carlo Simulation with three classes: die, game, and analyzer. In addition, there are unit tests, a scenario script, and documentation for the code. Created for DS5100 as a final project. 

# Metadata
- Name: Eric Tang
- Date: 7/15/2022
- Package: Monte Carlo Simulation
- Course: DS 5100

# Synopsis
## Installing and Importing
1. Download or clone the repository to your local machine.
2. Go into your terminal and change the working directory to the root of this directory.
3. From the terminal, execute the following code:

    pip install -e .
    
*Note the period at the end!
4. If everything is successful, you should see:

    Successfully installed Monte-Carlo-Simulation-1.0.0
    
Congratulations! Now, you're ready to use all this package has to offer.

To import the three classes into your project, go to your python file and at the top, type in:

    from montecarlo import Die, Game, Analyzer
            
This allows you to type in the methods without specifying the package (as the example code will demonstrate). This is the recommended way, but alternatively, you can simply import the package as so:

    import montecarlo

But using this will require specifying the montecarlo package whenever a method is needed to be called.
## Demo
### Using Die
To initalize a die (e.g. a regular die with six faces):

    newDie = Die([1,2,3,4,5,6])
    
To change the weight of a die (e.g. change the weight of face '6' to 5).

    newDie.change_weight(6, 5)
    
To roll the die (e.g. rolling 8 times):

    newDie.roll(8)

To get the results of the die roll:

    newDie.show()
    
### Using Game
To initalize a game (e.g. with three similar dices):

    newGame = Game([newDie, newDie, newDie])

To play the game (e.g. playing 10 different times):

    newGame.play(10)
    
To show the results of the game:

    newGame.show()

# Using Analyzer
To initalize an analyzer with a game:

    newAnalyzer = Analyzer(newGame)

To get the jackpot results from the analysis:

    newAnalyzer.jackpot()

To get the distinct combination of faces rolled:

    newAnalyzer.combo()
    
To get the face counts for each roll:

    testAnalyzer.face_counts_per_roll()

# Die Class API
Die with N sides, or “faces”, and W weights, and can be rolled to select a face. 

* Attributes
  - faces : list
    - a list of type string, float, or int representing faces of a die
* Methods

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

        A list of all classes with their public methods and attributes.
        Each item should show their docstrings.
        All paramters (with data types and defaults) should be described.
        All return values should be described.
        Do not describe private methods and attributes.
# Game API


# Analyzer API
# Manifest

    .gitignore
    LICENSE
    README.md
    montecarlo_demo.ipynb
    montecarlo_results.txt
    montecarlo_tests.py
    setup.py 
    montecarlo\
        __init__.py
        montecarlo.py
