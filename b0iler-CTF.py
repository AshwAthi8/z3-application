from z3 import *
import string
s = Solver()
name = [BitVec("name%d" % i, 32) for i in range(23)]
for i in range(len(name)):
        s.add(And(name[i] > 20 , name[i] <= 125))

s.add(And((name[0])==112),
    (name[1] ==99),
    (name[2] == 116),
    (name[3] == 102),
    (name[4] == 123),
    (name[5] == 115),
    (name[7] == 100),
    (name[8] == 95),
    (name[9] == 99),
    (name[15] == 95),
    (name[16] == 110),
    (name[19] == 122),
    (name[21] == 122),
    (name[22] ==125),
    (name[6] ==52 ),
    (name[14] == 52)
    )
s.add(And(name[6] >= 48,name[6]<=125))
s.add(And(name[10] >= 48,name[10]<=125))
s.add(And(name[11] >= 48,name[11]<=125))
s.add(And(name[12] >= 48,name[12]<=125))
s.add(And(name[13] >= 48,name[13]<=125))
s.add(And(name[14] >= 48,name[14]<=125))
s.add(And(name[17] >= 48,name[17]<=125))
s.add(And(name[18] >= 48,name[18]<=125))
s.add(And(name[20] >= 48,name[20]<=125))
s.add(And(name[22] >= 48,name[22]<=125))
s.add(And(name[4] >= 48,name[4]<=125))
s.add(And(name[8] >= 48,name[8]<=125))
s.add(And(name[2] >= 48,name[2]<=125))
s.add(And(name[3] >= 48,name[3]<=125))
s.add(name[8] == name[15])
s.add(name[13] == name[12])
s.add((name[8])+4 == ord('c'))
s.add(ord('{')-name[17]+40 == name[11])
s.add((name[17]+name[11] - name[5] - name[18]) == (name[18]-name[17]))
#s.add(name[0] == ((name[18]-name[17])*((name[6]-name[17])>>1)+ord('n')))
s.add(name[13] + 1 == name[10])
s.add(4*(ord('{')-ord('d')) + 2*(name[6]-name[17]) +(name[6]-name[17]) == name[10])
s.add(2*(name[18]-name[17]) == name[20] - ord('c'))
s.add(name[5]^name[16] == 29)
s.add((name[6]-name[17]) == 4*(name[18]-name[17]))
s.add(name[14] == name[6])
#print s.check()
while(s.check() == sat):
    print("solving...")
    m= s.model()
    w = ''
    for i in range(23):
        w += chr(m[name[i]].as_long())
    print(w)
    s.add(Or(name[0] != s.model()[name[0]],
             name[1] != s.model()[name[1]],
             name[2] != s.model()[name[2]],
             name[3] != s.model()[name[3]],
             name[4] != s.model()[name[4]],
             name[5] != s.model()[name[5]],
             name[6] != s.model()[name[6]],
             name[7] != s.model()[name[7]],
             name[8] != s.model()[name[8]],
             name[9] != s.model()[name[9]],
             name[10] != s.model()[name[10]],
             name[11] != s.model()[name[11]],
             name[12] != s.model()[name[12]],
             name[13] != s.model()[name[13]],
             name[14] != s.model()[name[14]],
             name[15] != s.model()[name[15]],
             name[16] != s.model()[name[16]],
             name[17] != s.model()[name[17]],
             name[18] != s.model()[name[18]],
             name[19] != s.model()[name[19]],
             name[20] != s.model()[name[20]],
             name[21] != s.model()[name[21]],
             name[22] != s.model()[name[22]]))

