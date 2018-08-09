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

# ignore states that are not reachable
def ignoreNotReachable(listOfVerticles, listOfStartingVerticles, listOfEndingVerticles, graph):
    # initialize the reachable array with zero
    isVerticleReachable = {}
    for vertex in graph:
        isVerticleReachable[vertex] = 0

    # with breadth-first search we determine which states are reachable
    reachables = set()
    for vertex in listOfStartingVerticles:
        edges = list(nx.bfs_edges(graph, vertex))
        nodes = [vertex] + [v for u, v in edges]
        for element in nodes:
            reachables.add(element)

    # actualize the reachable array
    for vertex in reachables:
        isVerticleReachable[vertex] = 1

    # remove from the graph the states that are not reachable
    for vertex in list(graph):
        if isVerticleReachable[vertex] != 1:
            graph.remove_node(vertex)

    for vertex in list(listOfVerticles):
        if isVerticleReachable[vertex] != 1:
            listOfVerticles.remove(vertex)

    for vertex in list(listOfStartingVerticles):
        if isVerticleReachable[vertex] != 1:
            listOfStartingVerticles.remove(vertex)

    for vertex in list(listOfEndingVerticles):
        if isVerticleReachable[vertex] != 1:
            listOfEndingVerticles.remove(vertex)

    return graph

# ignore states that are not productive
def ignoreNotProductive(listOfVerticles, listOfStartingVerticles, listOfEndingVerticles, graph):
    # we reverse the graph
    reversedGraph = graph.reverse()
    edges = list(reversedGraph.edges(data = True))

    # starting states -> ending states; ending states -> starting states
    newlistOfStartingVerticles = listOfEndingVerticles
    newlistOfEndingVerticles = listOfStartingVerticles

    ignoreNotReachable(listOfVerticles, newlistOfStartingVerticles, newlistOfEndingVerticles, reversedGraph)
    graph = reversedGraph.reverse()
    listOfStartingVerticles = newlistOfEndingVerticles
    listOfEndingVerticles = newlistOfStartingVerticles
    return graph

# write the new graph to file
def writeToFile(listOfVerticles, dictionary, listOfStartingVerticles, listOfEndingVerticles, graph):
    f = open('output.txt', 'w+')
    f.write(' '.join(map(str, listOfVerticles)) + '\n')
    f.write(' '.join(map(str, dictionary)) + '\n')
    f.write(' '.join(map(str, listOfStartingVerticles)) + '\n')
    f.write(' '.join(map(str, listOfEndingVerticles)) + '\n')

    edges = list(graph.edges(data = True))
    for e in edges:
        label = list(e[2].values())
        f.write(e[0] + ' ' + label[0]  + ' ' + e[1] + '\n')

    f.close()

# usage message
def usage(scriptName):
    print('Usage: ' + scriptName + ' [-i <inputfilename>] [-o <outputfilename>]')

def main(argv):
    # argument parse
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "input=", "output="])
    except getopt.GetoptError as err:
        print('Usage: ' + argv[0] + ' [-i <inputfilename>] [-o <outputfilename>]')
        print(err)
        sys.exit(2)
    inputFile = None
    outputFile = None
    for o, a in opts:
        if o in ("-h", "--help"):
            print('Usage: ' + argv[0] + '[-i <inputfilename>] [-o outputfilename]')
            sys.exit()
        elif o in ("-i", "--input"):
            inputFile = a
            print('Input file: ' + a)
        elif o in ("-o", "--output"):
            outputFile = a
            print('Output file: ' + a)
        else:
            assert False, "unhandled option"
    if (inputFile == None):
        usage(argv[0])
        sys.exit()
    if (outputFile == None):
        usage(argv[0])
        sys.exit()

    # plot the original graph
    Popen(['python', 'plot.py',  inputFile])

    G = nx.DiGraph()

    # input
    f = open(inputFile, 'r')

    # read in the vertices
    line = f.readline()
    listOfVerticles = line.split()

    # read in the characters
    line = f.readline()
    dictionary = line.split()

    # read in the starting states
    line = f.readline()
    listOfStartingVerticles = line.split()

    # read in the ending states
    line = f.readline()
    listOfEndingVerticles = line.split()

    # read in the edges
    for line in f:
        myList = line.split()
        G.add_edge(myList[0], myList[2], label=myList[1])
    f.close()

    # ignore not reachable and not productive states
    G = ignoreNotReachable(listOfVerticles, listOfStartingVerticles, listOfEndingVerticles, G)
    G = ignoreNotProductive(listOfVerticles, listOfStartingVerticles, listOfEndingVerticles, G)
    writeToFile(listOfVerticles, dictionary, listOfStartingVerticles, listOfEndingVerticles, G)

    # plot the resulting graph
    Popen(['python', 'plot.py', outputFile])

if __name__ == "__main__":
    main(sys.argv)
