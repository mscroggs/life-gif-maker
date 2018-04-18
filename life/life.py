class Life:
    def __init__(self):
        self.alive = []

    def __setitem__(self,pos,n):
        if n:
            if pos not in self.alive:
                self.alive.append(pos)
        else:
            if pos in self.alive:
                self.alive.remove(pos)

    def __getitem__(self, pos):
        for p in self.alive:
            if p[0] == pos[0] and p[1] == pos[1]:
                return True
        return False

    def get_limits(self):
        xmin = None
        xmax = None
        ymin = None
        ymax = None
        for x,y in self.alive:
            if xmin is None:
                xmin = x
                xmax = x
                ymin = y
                ymax = y
            else:
                xmin = min(x,xmin)
                xmax = max(x+1,xmax)
                ymin = min(y,ymin)
                ymax = max(y+1,ymax)

        return xmin, xmax, ymin, ymax

    def add(self, pattern, pos=(0,0)):
        pattern.add(self, pos)

    def export(self, filename, limits=None):
        import matplotlib.pylab as plt
        plt.style.use('dark_background')
        if limits is None:
            xmin, xmax, ymin, ymax = self.get_limits()
        else:
            xmin, xmax, ymin, ymax = limits
        for x in range(xmin,xmax+1):
            plt.plot([x,x],[ymin,ymax],"w-")
        for y in range(ymin,ymax+1):
            plt.plot([xmin,xmax],[y,y],"w-")
        for x,y in self.alive:
            if xmin <= x < xmax and ymin <= y < ymax:
                plt.fill([x,x+1,x+1,x,x],[y,y,y+1,y+1,y],"w")

        plt.tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off')
        plt.tick_params(axis='y',which='both',left='off',right='off',labelleft='off')

        plt.axis("equal")
        plt.box("off")
        plt.savefig(filename)
        plt.clf()

    def next(self):
        new_alive = []
        xmin, xmax, ymin, ymax = self.get_limits()
        if xmin is not None:
            for x in range(xmin-1,xmax+2):
                for y in range(ymin-1,ymax+2):
                    n = 0
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if self[x+i,y+j]:
                                n += 1
                    if self[x,y] and 3 <= n <= 4:
                        new_alive.append((x,y))
                    if not self[x,y] and n == 3:
                        new_alive.append((x,y))
        self.alive = new_alive
