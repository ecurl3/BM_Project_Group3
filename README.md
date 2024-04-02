# Bipartite Matching Problem - Group 3

## Gale-Shapley algorithm
This is an algorithm that is used within this program to find stable matches between men and women based off of their preference list. More detailed information can be found about this algorithm [here.](https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm)

## Input Graph structure
The Gale-Shapley algorithm takes in a graph as input which is produced at random within this program. However, the amount of people represented in it is determined by the user (See `How to Run`). An important thing to note is that the input graph will end up having `2*n` rows to represent `n` males and `n` females. An example of when the user inputs `3` while executing can be seen below:

```
3 4 5
5 3 4
4 3 5
0 1 2
2 0 1
1 0 2
```

Each `ith` row represents someone's preference list but rows `0` to `2` represent Males, and rows `3` to `5` represent Females.

## Installing Python
This program has been tested on `Python 3.12.2`. You can use other versions (preferably later ones), but there may be bugs.

Make sure Python is installed on your machine by checking with this command:
```python3 --version```

If you don't have python3, you can install it [here.](https://www.python.org/downloads/)

## How to Run
You can run this program by simply performing the example command below. Please note that you must enter a number into the argument.
```
./main.py 5
```

If you create a new python file, you might get the error message `zsh: permission denied: ./example.py`. To fix this use the command:
```
chmod a+x example.py
```
You can now run the program

# Group Members

## Leader
Anastasia Spencer
## Animation
Nate Paul  
Anastasia Spencer  
## Algorithm Implementation
Jacob Santos  
Tyler Coleman  
Emily Curl
## Testing and Debugging
Brooke Boskus
Daniel Tsark
## Presentation
Lucas Underbakke

