# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver (already solved by me)

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: By eliminating values using the naked twins strategy. Let's say that there is two boxes of the same two possible values, and are equal, then are locked in those two boxes. Therefore, no other box in their same unit.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: I added 2 main diagonal units to the unit list (unitlist). By going through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers of the same diagonal.

### Install

This project requires **Python 3**.

I recommend you install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment provided for unix or windows:
Unix env => aind-environment-unix
Windows env => aind-environment-windows

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Data

The data consists of a text file of diagonal sudokus for you to solve.
