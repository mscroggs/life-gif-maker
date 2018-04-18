from life import Life
from patterns import gun

p = Life()
p.add(gun)

for i in range(1,46):
    p.export("output/gun-frame"+str(i)+".png",)
    p.next()
