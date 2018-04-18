class Pattern:
    def cells(self):
        return []

    def add(self, life, pos=(0,0)):
        for x,y in self.cells():
            life[pos[0]+x,pos[1]+y] = True

