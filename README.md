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
    - List of type string, float, or int representing faces of a die
* Methods
  - __init__(faces):
    - Creates a Die object with an array of faces and initalizes a list of equal weights of 1 for each face.
  - change_weight(face, weight):
    -  Checks if the face passed is initalized in the Die and if the weight is a float or int. Changes the weight of a single side.
  - roll(r = 1):
    - Rolls the dice r times, defaulting to one. Returns a list of rolled outcomes.
  - show():
    - Returns a dataframe of the die's current set of faces and weights


        A list of all classes with their public methods and attributes.
        Each item should show their docstrings.
        All paramters (with data types and defaults) should be described.
        All return values should be described.
        Do not describe private methods and attributes.
# Game API
A game consisting of rolling one or more dice of the same kind one or more times

* Attributes
  - dice : list
    - a list of type Die, representing the different dices to roll
* Methods
  - __init__(dice):
    - Creates a Game object with an array of Die objects.
  - play(n = 1):
    -  Takes a parameter to specify how many times the dice should be rolled, defaulting to 1.

  - show(form = 'wide')::
    - Returns the result from playing in a dataframe. Requires calling the play() method first to work.
    - Allows specification of form. Narrow form is a two-column index with the roll number and the die number, and a column for the face rolled. Wide form is a single column index with the roll number, and each die number as a column.

# Analyzer API
Analyzer takes the results of a single game and computes various descriptive statistical properties. 
* Attributes
  - game : Game
    - Game that is to be analyzed
  - gameType : Type
    - Type of faces on the dice used in the game. Can be string, int, or float.
  - jackpot_result : DataFrame
    - DataFrame of all rolls resulting in identical faces. Requires calling jackpot().
  - combo_result : DataFrame
    - DataFrame of all unique combinations and their counts. Requires calling combo().
  - face_per_roll : DataFrame
    - DataFrame of the counts of all faces in each roll. Requires calling face_counts_per_roll().
* Methods
  - __init__(game):
    - Initalizes an Analyzer object with a game. Also records the data type of the die faces used.
  - jackpot()
    - Records the rolls resulting in identical faces in a dataframe of jackpot results as a public attribute.
    - Returns an integer for the number times the game resulted in all faces being identical.
  - combo()
    - Records the distinct combinations of faces rolled in a public attribute, along with their counts.       
    - Returns the dataframe of results
  - face_counts_per_roll()
    - Records the times a face is rolled in each event and stores the results in a DataFrame.
    - Each face value has their own distinct column and the index is the roll number in the DataFrame.
    - Returns the dataframe of results.   

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
