# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

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
* `Unix env` - sudoku-ai-environment-unix.yml
* `Windows env` - sudoku-ai-environment-windows.yml

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Data

The data consists of a text file of diagonal sudokus for you to solve.

### Code
* `solutions.py` - This is where we solve the sudoku problem.
* `solution_test.py` - You can test the solution by running `python solution_test.py`. If you need to add more test cases, please feel free to add more.

### Run the code on virtual env
* `Create env` - conda env create -f sudoku-ai-environment-unix.yml
* `Activate the env` - source activate aind
* `Run the unit test` - python solution_test.py (Please make sure you are in the project folder. Check 'pwd' command)
* `Deactivate the env` - source deactivate aind

### Dependecies
- mkl=2017.0.1=0
- numpy=1.11.3=py36_0
- openssl=1.0.2j=0
- pip=9.0.1=py36_1
- python=3.6.0=0
- readline=6.2=2
- scikit-learn=0.18.1=np111py36_1
- scipy=0.18.1=np111py36_1
- setuptools=27.2.0=py36_0
- sqlite=3.13.0=0
- tk=8.5.18=0
- wheel=0.29.0=py36_0
- xz=5.2.2=0
- zlib=1.2.8=3
- pip:
  - hmmlearn==0.2.0
