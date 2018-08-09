''' 
MIT License

Copyright (c) 2018 Biro Eniko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''
from graphviz import Digraph
import sys

def main(fileName):
    dot = Digraph()

    # input
    f = open(fileName, 'r')

    # read in the states
    line = f.readline()
    listOfVerticles = line.split()
    for vertex in listOfVerticles:
        dot.node(vertex, vertex, shape='circle')

    # read in the characters
    line = f.readline()
    dictionary = line.split()

    # read in the starting states
    line = f.readline()
    listOfStartingVerticles = line.split()
    for vertex in listOfStartingVerticles:
        dot.node('0' + vertex, shape='none', style='invisible')
        dot.edge('0' + vertex, vertex)

    # read in the ending states
    line = f.readline()
    listOfEndingVerticles = line.split()
    for vertex in listOfEndingVerticles:
        dot.node(vertex, shape='doublecircle')

    # read in the edges
    for line in f:
        myList = line.split()
        dot.edge(myList[0], myList[2], myList[1])
        
    dot.render('output/automata' + fileName + '.gv', view=True)

if __name__ == "__main__":
    main(sys.argv[1])
