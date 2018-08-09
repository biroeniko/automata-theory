# Automata theory exercises

Some example codes for automata theory exercises

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The basic requirements for building the executable are:

* Python 3
* pip3
* graphviz + python-pydot
* matplotlib
* networkx

#### Installation on Ubuntu

```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt install python-pydot python-pydot-ng graphviz
sudo apt-get install python3-matplotlib
pip3 install networkx
```
NOTE: this code was also tested with Python 2.7, with the corresponding packages 

### Installing

This program have been tested on Ubuntu 16.04 but should work under any systems that fulfills the aforementioned requirements.

#### Installation on Ubuntu

If you succesfully cloned the source files and you are currently in the project directory, you can simply run the script file by typing in the command line:

```
python3 ignoreNotOK.py -i graph1.txt -o output.txt
```
You can also make your own graph files, defining the graph in the input file as follows: 
1. row: all states, separated by spaces
2. row: elements of the input dictionary, separated by spaces
3. row: starting states, separated by spaces
4. row: ending states, separated by spaces
5. row: one transition per line, separated by spaces (state input state)

Now, you should see the executable in the build file. If you run the executable, the application should look like this:
![](https://github.com/biroeniko/mandelbrot/blob/master/img/demo.png)

## Built With

* [SDL2](https://www.libsdl.org/) - used for display and control
* [OpenMP](https://www.openmp.org/) - used for creating multiple threads for the tasks (pixel color calculation)

## Authors

* **Biró Enikő** - [BiroEniko](https://github.com/biroeniko)