class Monitor:
    def __init__(self, Seq):
        print "Monitor initialized ..."
        self.Seq = Seq
        self.record = []

    def insert(self, low, high):
        print "Inserted #(low,high)=(%5d,%5d) ..." % (low, high)
        
        self.record.append([low, high])

    def show_record(self):
        for idx,_tuple in enumerate(self.record):
            #print "#record=%5d high=%5d low=%5d" % (idx, _tuple[0], _tuple[1])
            high = _tuple[1]
            low  = _tuple[0]
            List = self.Seq

            print "[",
            for idx, val in enumerate(List):
                print val,
                if idx == high:
                    print "(h)",
                if idx == low:
                    print "{l}",
                if idx == low + (high-low)/2:
                    print "*mid*",

                if idx != len(List)-1:
                    print ",",
            print "]"

    def clear(self):
        self.record = []

