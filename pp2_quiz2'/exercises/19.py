import math
x1,x2,x3 = map(int,input().split())
y1,y2,y3 = map(int,input().split())
formula = math.sqrt((x2-x1)**2+(y2-y1)**2+(x3-y3)**2)
print(formula)

