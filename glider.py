from life import Life
from patterns import glider

p = Life()
p.add(glider)

for i in range(1,46):
    p.export("output/glider-frame"+str(i)+".png",[3,12,3,12])
    p.next()
