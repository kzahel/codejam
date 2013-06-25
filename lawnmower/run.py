import sys

class Lawn:
    def __init__(self, w, h, data):
        self.w = w
        self.h = h

        self.max_fixed_x = []
        self.max_fixed_y = []

        self.data = data

    def __repr__(self):
        s = '\nLAWN %s %s' % (self.w, self.h)
        for line in self.data:
            s += '\n' + ' '.join(map(str,line))
        return s

    def prepare(self):
        for x in range(self.w):
            m = max( self.data[y][x] for y in range(self.h) )
            self.max_fixed_x.append( m )

        for y in range(self.h):
            self.max_fixed_y.append( max( self.data[y][x] for x in range(self.w) ) )

    def is_valid(self):
        self.prepare()

        #print 'maxes_x',self.max_fixed_x, 'maxes_y',self.max_fixed_y

        for y in range(self.h):
            for x in range(self.w):
                valhere = self.data[y][x]
                if valhere < self.max_fixed_x[x] and \
                   valhere < self.max_fixed_y[y]:
                    #print 'invalid at',[x,y]
                    return False

        return True


def iterlawns(filename):
    


    with open(filename) as f:
        numtestcases = int(f.readline().strip())
        numread = 0

        while numread < numtestcases:
            l = f.readline().strip().split(' ')
            #print 'read l',l
            h, w = map(int, l)
            data = [map(int,f.readline().strip().split(' ')) for _ in range(h)]
            lawn = Lawn(w,h, data )
            #print '\ngot lawn',lawn
            #print 'new lawn',lawn
            yield lawn
            numread += 1

        

if __name__ == '__main__':
    lawns = iterlawns(sys.argv[1])


    if False:
        i = 0
        while i < 10:
            lawn = lawns[i]
            print lawn
            print lawn.is_valid()
            i += 1

    for n,lawn in enumerate(lawns):
        print 'Case #%s: %s' % (n+1, 'YES' if lawn.is_valid() else 'NO')

    #print data
