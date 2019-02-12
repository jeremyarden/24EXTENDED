import sys
import backend24 as Backend

def main():
    
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    inp = open("%s" % inputFile, "r") 
    numList = inp.read().split()
    newList = list(map(int, numList))

    opList = Backend.calc(newList)
    mathEx = Backend.satuinAngkaOp(newList, opList)
    res = mathEx + '=' + str(eval(mathEx))
    
    out = open("%s" % outputFile, "w")
    out.write(res)

main()