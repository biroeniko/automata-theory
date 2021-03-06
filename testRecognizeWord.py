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
import sys

def main(argv):
    myFile = 'testgraph.txt'
    # plot the original graph
    Popen(['python3', 'plot.py', myFile])

    myTestFile = 'words.txt'
    f = open(myTestFile, 'r')

    # read in the words
    for line in f:
        myWord = line.split()
        print(str(myWord[0]))
        p = Popen(['python3', 'recognizeWord.py', '-w', str(myWord[0]), '-i', myFile])
        p.communicate()
    f.close()

if __name__ == "__main__":
    main(sys.argv)
