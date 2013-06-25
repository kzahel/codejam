import sys
import copy

class Board:
    def __init__(self, d, data):
        self.d = d
        self.d2 = pow(d,2)
        self.data = data

    def __repr__(self):
        s = '\nBoard %s' % self.d
        for line in self.data:
            s += '\n' + ''.join(['-' if c is None else str(c) for c in line])
        return s

    def check_is_invalid(self):
        # checks whether board is already invalid
        return False

    def check_no_moves(self):
        #print 'check_no_moves', self
        for x in range(self.d2):
            for y in range(self.d2):
                if self.data[y][x] == None:
                    return False
        return True
        

    def legal_moves_at(self, x, y):
        # returns all legal digit placements at x, y
        x_fixed = set( self.data[cy][x] for cy in range(self.d2) ).difference([None])
        y_fixed = set( self.data[y][cx] for cx in range(self.d2) ).difference([None])

        s_x = x / self.d
        s_y = y / self.d

        mysquare = set( self.data[s_y*self.d + cy][s_x*self.d + cx] for cx in range(self.d) for cy in range(self.d) ).difference([None])



        #print 'legal moves at',x,y,'_x',x_fixed,'_y',y_fixed,'mysquare',mysquare

        un = mysquare.union(x_fixed).union(y_fixed)
        toret = set(range(self.d2)).difference( un )
        #print 'legal moves at',x,y,toret
        return toret
        


    def has_solution(self):
        # depth first search in solution space

        if self.check_is_invalid():
            # should not have to check this unless input board is invalid
            return False

        if self.check_no_moves():
            print 'have solution!', self
            return True



        minchoice = None
        minchoiceval = None

        for x in range(self.d2):
            for y in range(self.d2):
                if self.data[y][x] == None:
                    #print 'found None at',x,y, self
                    placements = self.legal_moves_at(x, y)
                    if len(placements) == 0:
                        #print 'no placements at!',x,y
                        return False

                    if minchoiceval is None or len(placements) < minchoiceval:
                        minchoiceval = len(placements)
                        minchoice = (x,y)

                        
        x,y = minchoice
        
        for placement in self.legal_moves_at(x,y):

            #print 'iter legal move at',x,y,placement,self

            datacopy = copy.deepcopy(self.data)

            datacopy[y][x] = placement
            b = Board(self.d, datacopy)

            if b.has_solution():
                return True




def parse(line):
    cs = [c for c in list(line) if c != ' ']
    cs = [None if c == '_' else int(c) for c in cs]
    return cs

def iterboards(filename):

    with open(filename) as f:
        numtestcases = int(f.readline().strip())
        numread = 0

        while numread < numtestcases:
            dim = int(f.readline().strip())
            numdigits = pow(dim,2)
            numlines = numdigits + dim - 1

            data = [f.readline().strip() for _ in range(numlines)]
            data = [l for l in data if l]
            data = [parse(l) for l in data]

            yield Board(dim,data)
            numread += 1
            #for g in range(dim):
                #[f.readline() for _ in range(dim)]

if __name__ == '__main__':
    bs = iterboards(sys.argv[1])
    for n,board in enumerate(bs):
        print board
        print board.has_solution()


