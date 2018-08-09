# Automata theory exercises

Some example codes for automata theory exercises

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The basic requirements for building the executable are:

* Python 3
* pip3
* graphviz + python-pydot
* networkx

#### Installation on Ubuntu

```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt install python-pydot python-pydot-ng graphviz
pip3 install networkx
```
NOTE: this code was also tested with Python 2.7, with the corresponding packages 

### Installing

This program have been tested on Ubuntu 16.04 but should work under any systems that fulfills the aforementioned requirements.

## Usage instructions

There are several example programmes, each of which uses the following input file standards for representing the graphs:
1. row: all states, separated by spaces
2. row: elements of the input dictionary, separated by spaces
3. row: starting states, separated by spaces
4. row: ending states, separated by spaces
5. row: one transition per line, separated by spaces (state input state)

If you succesfully cloned the source files and you are currently in the project directory, you can simply run the script files.

### Ignore not reachable and not productive vertices from the graph
For running the script, you have to provide the input and output files. The input file contains the graph in the aforementioned representation, the output file will contain the resulting graph.
```
python3 ignoreNotOK.py -i graph1.txt -o output.txt
```
## Built With

* [graphviz](https://www.graphviz.org/) - used for displaying the graphs
* [networkx](https://networkx.github.io/) - data structure for digraph

## Authors

* **Biró Enikő** - [BiroEniko](https://github.com/biroeniko)
