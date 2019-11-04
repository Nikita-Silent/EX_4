import local as lc
import loc_ru as lr
s = []
loc = input(lc.LC).lower()
if loc == lc.EN:
    ans = input(lc.TXT_0).lower()
    fill = input(lc.TXT_1).lower()
    if ans == lc.ANS_1:
        for i in range(len(fill)):
            for j in range(lc.NUM):
                if fill[i] == lc.AZBUKA_EN[j]:
                    s.append(lc.AZBUKA_EN[j+1])
        print(''.join(s))
    elif ans == lc.ANS_2:
        for i in range(len(fill)):
            for j in range(lc.NUM):
                if fill[i] == lc.AZBUKA_EN[j]:
                    s.append(lc.AZBUKA_EN[j - 1])
        print(''.join(s))
    else:
        print(lc.ER)


elif loc == lc.RU:
    ans = input(lr.TX_0).lower()
    fill = input(lr.TX_1).lower()
    if ans == lr.AN_1:
        for i in range(len(fill)):
            for j in range(lr.NUM_1):
                if fill[i] == lr.AZBUKA_RU[j]:
                    s.append(lr.AZBUKA_RU[j + 1])
        print(''.join(s))
    elif ans == lr.AN_2:
        for i in range(len(fill)):
            for j in range(lr.NUM_1):
                if fill[i] == lr.AZBUKA_RU[j]:
                    s.append(lr.AZBUKA_RU[j - 1])
        print(''.join(s))
    else:
        print(lr.ER_1)

else:
    print(lc.ER)
