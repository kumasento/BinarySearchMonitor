import os
import sys
import random

import binarysearch as bs
import monitor as mon

def ListGen(lower_bound, upper_bound, number_bound):
    if number_bound <= 0:
        return []
    result = []
    for i in range(number_bound):
        result.append(
                random.randint(
                        lower_bound, 
                        upper_bound)
                )
    return sorted(result)

def TarGen(List):
    inList = True
    #if random.randint(0, 1) == 0:
    #    inList = False

    if inList:
        idx = random.randint(0, len(List)-1)
        tar = List[idx]
    else:
        low  = List[0]-1
        high = List[-1]+1
        tar  = random.randint(low, high)
    #    while (tar in List):
    #        tar = random.randint(low, high)
        
    return tar

if __name__ == '__main__':
    Argv = sys.argv[1:]
    Argc = len(sys.argv)
    
    number_bound = 100
    lower_bound = 1
    upper_bound = 1000
    if Argc > 1:
        number_bound = int(Argv[0])
        lower_bound  = int(Argv[1])
        upper_bound  = int(Argv[2])
        
        #if number_bound > (upper_bound - lower_bound + 1):
        #    print "number bound should be less than the range of sequence"
        #    exit(1)

    List = ListGen(lower_bound, upper_bound, number_bound)
    Target = TarGen(List)
    print "List->"+str(List)
    print "Val ->"+str(Target)

    #print List, Target
    
    monitor = mon.Monitor(List)

    print "Testing 'regular' binary search ..."
    ResultIdx = bs.regular(List, Target, monitor)
    print "->Record List:"
    monitor.show_record()
    if ResultIdx >= 0:
        print "#index=%3d" % ResultIdx
        print "find=%5d : real=%5d" % (List[ResultIdx], Target)    
    else:
        print "No answer founded"
        for elem in List:
            if elem == Target:
                print "[ERROR] There's such element in List: " + str(List)

    print "Testing 'lowerbound' binary search ..."
    ResultIdx = bs.lowerbound(List, Target, monitor)
    print "->Record List:"
    monitor.show_record()
    if ResultIdx >= 0:
        print "#index=%3d" % ResultIdx
        print "find=%5d : real=%5d" % (List[ResultIdx], Target)    
    else:
        print "No answer founded"
        for elem in List:
            if elem == Target:
                print "[ERROR] There's such element in List: " + str(List)

    print "Testing 'upperbound' binary search ..."
    ResultIdx = bs.upperbound(List, Target, monitor)
    print "->Record List:"
    monitor.show_record()
    if ResultIdx >= 0:
        print "#index=%3d" % ResultIdx
        print "find=%5d : real=%5d" % (List[ResultIdx], Target)    
    else:
        print "No answer founded"
        for elem in List:
            if elem == Target:
                print "[ERROR] There's such element in List: " + str(List)
