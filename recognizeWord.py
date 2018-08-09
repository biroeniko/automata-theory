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

from subprocess import Popen
import networkx as nx
import sys, getopt

def multiplication(matrix1, matrix2):
    # matrix multiplication
    size = len(matrix1)
    result = [[0 for x in range(size)] for y in range(size)]

    # iterate through rows of X
    for i in range(len(matrix1)):
       # iterate through columns of Y
       for j in range(len(matrix2[0])):
           # iterate through rows of Y
           for k in range(len(matrix2)):
               result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def recognizeWord(graph, listOfVerticles, dictionary, listOfStartingVerticles, listOfEndingVerticles, myWord):
    size = len(listOfVerticles)
    edges = list(graph.edges(data = True))
    matrix = [[0 for x in range(size)] for y in range(size)]

    # vertex - matrix corresponding:
    naming = {}
    index = 0
    for vertex in graph:
        naming[vertex] = index
        index = index + 1

    # renaming the vertices in the list corresponding to the transcripting rules
    newListOfStartingVerticles = []
    for e in listOfStartingVerticles:
        newListOfStartingVerticles.append(naming[e])
    newListOfEndingVerticles = []
    for e in listOfEndingVerticles:
        newListOfEndingVerticles.append(naming[e])

    # checking a word with matrix multiplication
    index = 0
    for letter in list(myWord):
        matrix = [[0 for x in range(size)] for y in range(size)]
        for e in edges:
            label = list(e[2].values())
            if (label[0] == letter):
                matrix[naming[e[0]]][naming[e[1]]] = 1

        if index == 0:
            prevMatrix = matrix
        else:
            prevMatrix = multiplication(prevMatrix, matrix)
        index = index + 1
    
    # check that the vertex of the row is a starting vertex and the vertex in the column is an ending vertex
    for i in range(size):
        for j in range(size):
            if (prevMatrix[i][j] != 0 and i in newListOfStartingVerticles and j in newListOfEndingVerticles):
                return True
    return False

# usage message
def usage(scriptName):
    print('Usage: python3 ' + scriptName + ' [-w <word>] [-i <inputfilename>]')

def main(argv):

    # argument parse
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:w:", ["help", "input=", "word="])
    except getopt.GetoptError as err:
        usage(argv[0])
        print(err)
        sys.exit(2)
    inputFile = None
    inputWord = None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage(argv[0])
            sys.exit()
        elif o in ("-i", "--input"):
            inputFile = a
            print('Input file: ' + a)
        elif o in ("-w", "--word"):
            inputWord = a
            print('Input word: ' + a)
        else:
            assert False, "unhandled option"
    if (inputFile == None):
        usage(argv[0])
        sys.exit()
    if (inputWord == None):
        usage(argv[0])
        sys.exit()

    G = nx.DiGraph()

    # read in file
    f = open(inputFile, 'r')

    # read in states
    line = f.readline()
    listOfVerticles = line.split()

    # read in characters
    line = f.readline()
    dictionary = line.split()

    # read in starting states
    line = f.readline()
    listOfStartingVerticles = line.split()

    # read in ending states
    line = f.readline()
    listOfEndingVerticles = line.split()

    # read in transitions
    for line in f:
        myList = line.split()
        G.add_edge(myList[0], myList[2], label=myList[1])
    f.close()

    #nodes = list(G.nodes)
    isrecognized = recognizeWord(G, listOfVerticles, dictionary, listOfStartingVerticles, listOfEndingVerticles, inputWord)
    print("The word is recognized by the automata: " + str(isrecognized))

if __name__ == "__main__":
    main(sys.argv)
