from life import Life

p = Life()
p[0,0] = True
p[1,1] = True
p[2,1] = True
p[0,2] = True
p[1,2] = True

for i in range(1,46):
    p.export("frame"+str(i)+".png",[3,12,3,12])
    p.next()
