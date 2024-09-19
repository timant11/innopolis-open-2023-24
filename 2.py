order =  'ABCDCB'
children = 0
a = int(input())
b = int(input())
c = int(input())
d = int(input())
summ = a+b+c+d
i_=0
for i in range(summ):
    if i_ > 5:
        i_ = 0
    if order[i_] == 'A':
        if a>0:
            a-=1
        else:
            break
    elif order[i_] == 'B':
        if b>0:
            b-=1
        else:
            break
    elif order[i_] == 'C':
        if c>0:
            c-=1
        else:
            break
    elif order[i_] == 'D':
        if d>0:
            d-=1
        else:
            break
    children += 1
    i_ += 1
print(children)